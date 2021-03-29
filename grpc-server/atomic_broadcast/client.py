
import socket
UDP_IP = "127.0.0.1"

UDP_PORT = 5000
UDP_PORT1 = 5001
UDP_PORT2 = 5002
UDP_PORT3 = 5003
UDP_PORT4 = 5004

UPD_PORTS = [5000, 5001, 5002, 5003, 5004]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

for port in UPD_PORTS:
    MESSAGE = b"Hello, World!"

    print("UDP target IP: %s" % UDP_IP)

    print("UDP target port: %s" % port)
    print("message: %s" % MESSAGE)
    sock.sendto(MESSAGE, (UDP_IP, port))