import socket
import json
from models import Register, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from customerdbOperations import dbops

UDP_IP = "127.0.0.1"

UDP_PORT = 5004
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
local_seq_num = 0
global_seq_num = 0
proc_no = 4
sender_id = 234
sock.bind((UDP_IP, UDP_PORT))

send = []
recieve = []
recieveBuffer = []
sendBuffer = []

engine = create_engine('mysql+pymysql://root:pass@host.docker.internal:3329/onlineshopping')
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = DBSession()

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    if (json.loads(data.decode("utf-8"))["type"] == "client"):
        message = {"local_seq_num": local_seq_num, "data": data.decode("utf-8"), "sender_id": sender_id,
                   "type": "receiveMessage"}
        sock.sendto(json.dumps(message).encode(), (UDP_IP, 5010))

    else:
        print("received message: %s" % data)
        message = json.loads(data.decode("utf-8"))
        if(message["type"] == "receiveMessage" and (((global_seq_num + 1) % 5) == proc_no)):
            if(not recieve or (recieve[-1] + 1 == global_seq_num + 1)):
                if(not recieveBuffer):
                    global_seq_num += 1
                    local_seq_num = global_seq_num
                    print("updated global sequence to {number}".format(number=global_seq_num))
                    message = {"local_seq_num": local_seq_num, "data": message["data"], "sender_id": sender_id,
                               "global_seq_num": global_seq_num, "type": "sendMessage"}
                    sock.sendto(json.dumps(message).encode(), (UDP_IP, 5010))
                    sock.sendto(json.dumps(message).encode(), (UDP_IP, 5001))
                    sock.sendto(json.dumps(message).encode(), (UDP_IP, 5002))
                    sock.sendto(json.dumps(message).encode(), (UDP_IP, 5003))
                    send.append(global_seq_num)
                    dbops.createAccount(message["data"], session)
                else:
                    recieveBuffer.append(message)
                    while(not recieveBuffer):
                        message = recieveBuffer.pop(0)
                        global_seq_num += 1
                        local_seq_num = global_seq_num
                        print("updated global sequence to {number}".format(number=global_seq_num))
                        message = {"local_seq_num": local_seq_num, "data": message["data"], "sender_id": message["sender_id"],
                                   "global_seq_num": global_seq_num, "type": "sendMessage"}
                        sock.sendto(json.dumps(message).encode(), (UDP_IP, 5010))
                        sock.sendto(json.dumps(message).encode(), (UDP_IP, 5001))
                        sock.sendto(json.dumps(message).encode(), (UDP_IP, 5002))
                        sock.sendto(json.dumps(message).encode(), (UDP_IP, 5003))
                        send.append(global_seq_num)
                        dbops.createAccount(message["data"], session)
            else:
                print("adding message to buffer", message)
                recieveBuffer.append(message)


        elif(message["type"] == "sendMessage"):
            global_seq_num = message["global_seq_num"]
            local_seq_num = global_seq_num
            recieve.append(global_seq_num)
            dbops.createAccount(message["data"], session)
            # print("updated global squeuence to {number}".format(number=global_seq_num))