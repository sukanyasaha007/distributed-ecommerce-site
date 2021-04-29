import socket
import json
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from atomicBroadcastServer import AtomicBroadcast

UDP_IP = ["34.68.70.103", "35.224.252.120", "34.82.94.22"]
currentip = "0.0.0.0"

UDP_PORT = 5001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
local_seq_num = 0
global_seq_num = 0
proc_no = 1
sender_id = 456
sock.bind((currentip, UDP_PORT))

send = {}
recieve = {}
recieveBuffer = []
sendBuffer = []

engine = create_engine('mysql+pymysql://nmk:pass@35.184.209.79:3306/onlineshopping')
# engine = create_engine('mysql+pymysql://root:pass@host.docker.internal:3326/onlineshopping')
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = DBSession()
atomic_broadcast = AtomicBroadcast()

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes

    if (json.loads(data.decode("utf-8"))["type"] == "client"):
        message = {"local_seq_num": local_seq_num, "data": data.decode("utf-8"), "sender_id": sender_id,
                   "type": "receiveMessage"}
        data = json.dumps(message).encode()

    ports = [5010, 5002, 5003]
    local_seq_num, global_seq_num, recieve, recieveBuffer, send = \
        atomic_broadcast.recieveMessage(
        data, local_seq_num, global_seq_num, recieve,
        proc_no, recieveBuffer, sock, send,
        session, UDP_IP, ports, sender_id
    )