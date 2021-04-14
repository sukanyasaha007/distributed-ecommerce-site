import socket
import json
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from atomicBroadcastServer import AtomicBroadcast

# UDP_IP = "104.198.242.219"
# UDP_IP = ["0.0.0.0"]
UDP_IP = ["35.193.31.141", "34.122.75.220", "35.197.116.39"]
currentip = "0.0.0.0"
UDP_PORT = 5010
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
local_seq_num = 0
global_seq_num = 0
proc_no = 0
sender_id = 123
sock.bind((currentip, UDP_PORT))

send = {}
recieve = {}
recieveBuffer = []
sendBuffer = []

engine = create_engine('mysql+pymysql://nmk:pass@35.238.64.48:3306/onlineshopping')
# engine = create_engine('mysql+pymysql://root:pass@host.docker.internal:3325/onlineshopping')
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = DBSession()
atomic_broadcast = AtomicBroadcast()

if __name__ == "__main__":
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(data)
        if (json.loads(data.decode("utf-8"))["type"] == "client"):
            message = {"local_seq_num": local_seq_num, "data": data.decode("utf-8"), "sender_id": sender_id,
                       "type": "receiveMessage"}
            data = json.dumps(message).encode()
            # sock.sendto(json.dumps(message).encode(), (UDP_IP, 5001))

        ports = [5001, 5002, 5003]
        local_seq_num, global_seq_num, recieve, recieveBuffer, send = \
            atomic_broadcast.recieveMessage(
            data, local_seq_num, global_seq_num,recieve,
            proc_no, recieveBuffer, sock, send,
            session, UDP_IP, ports, sender_id
        )
