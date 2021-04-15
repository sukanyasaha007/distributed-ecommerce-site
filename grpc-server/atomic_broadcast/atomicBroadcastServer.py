import json
from customerdbOperations import dbops


class AtomicBroadcast():

    def checkMessage(self, message, session, sock):
        temp = json.loads(message["data"])
        if(temp["function"] == "createAccount"):
            dbops.createAccount(message["data"], session)
        if (temp["function"] == "login"):
            dbops.login(message["data"], session, sock, temp["ip"])
        if (temp["function"] == "addToCart"):
            dbops.addToCart(message["data"], session)
        if (temp["function"] == "updateproductQuantity"):
            dbops.updateproductQuantity(message["data"], session)

    def recieveMessage(self, data, local_seq_num, global_seq_num,
                       recieve, proc_no,
                       recieveBuffer, sock, send,
                       session, UDP_IP, ports, sender_id):
        print("received message: %s" % data)
        message = json.loads(data.decode("utf-8"))
        print(global_seq_num)
        if("data" in message):
            procs_active = json.loads(message["data"])["procs_active"]
            proc_no = json.loads(message["data"])["proc_no"]
            print("Yooooooo", global_seq_num + 1, procs_active, proc_no)

        if (message["type"] == "health"):
            sock.sendto(json.dumps({"health":"healthy"}).encode(), (message["ip"], 5005))

        elif (message["type"] == "receiveMessage" and (((global_seq_num + 1) % procs_active) == proc_no)):
            if (not recieve or (global_seq_num + 1 == (max(recieve) + 1))):
                if (not recieveBuffer):
                    global_seq_num += 1
                    local_seq_num = global_seq_num
                    print("updated global sequence to {number}".format(number=global_seq_num))
                    message = {"local_seq_num": local_seq_num, "data": message["data"], "sender_id": sender_id,
                               "global_seq_num": global_seq_num, "type": "sendMessage"}
                    for ip, i in zip(UDP_IP, ports):
                        sock.sendto(json.dumps(message).encode(), (ip, i))
                    send[global_seq_num] = (message)
                    self.checkMessage(message, session, sock)
                else:
                    recieveBuffer.append(message)
                    for k in range(max(recieve) + 1, global_seq_num+1):
                        message = {"global_seq_num": k,
                                   "type": "resendMessage"}
                        for ip, i in zip(UDP_IP, ports):
                            sock.sendto(json.dumps(message).encode(), (ip, i))

                    while (not recieveBuffer):
                        message = recieveBuffer.pop(0)
                        global_seq_num += 1
                        local_seq_num = global_seq_num
                        print("updated global sequence to {number}".format(number=global_seq_num))
                        message = {"local_seq_num": local_seq_num, "data": message["data"],
                                   "sender_id": message["sender_id"],
                                   "global_seq_num": global_seq_num, "type": "sendMessage"}
                        for ip, i in zip(UDP_IP, ports):
                            sock.sendto(json.dumps(message).encode(), (ip, i))
                        send[global_seq_num] = (message)
                        self.checkMessage(message, session, sock)
            else:
                print("adding message to buffer", message)
                recieveBuffer.append(message)

        elif (message["type"] == "sendMessage"):
            global_seq_num = message["global_seq_num"]
            local_seq_num = global_seq_num
            recieve[global_seq_num] = message
            self.checkMessage(message, session, sock)
            # print("updated global squeuence to {number}".format(number=global_seq_num))

        elif (message["type"] == "resendMessage" and (((message["global_seq_num"] + 1) % 5) == proc_no)):
            toSend = recieve[int(message["global_seq_num"])]
            for ip, i in zip(UDP_IP, ports):
                sock.sendto(json.dumps(toSend).encode(), (ip, i))

        return local_seq_num, global_seq_num, recieve, recieveBuffer, send