from datetime import datetime
import socket
import sys
from time import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 80)
# server_address = ('gosling-pro.duckdns.org', 80)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# try:
while True:
# Send data
    message = input('Type a message: ')
    print("you say {}  ({})".format(message,datetime.now()))
    message = message.encode('utf-8')
    sock.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = 1024
    data = sock.recv(1024)
    amount_received += len(data)
    if amount_received > 0:
        print('{} says {}  ({})'.format(server_address[0],data.decode('utf-8'),datetime.now()))
# except:
    # print('Socket closed')