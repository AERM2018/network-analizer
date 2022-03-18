from datetime import datetime
import socket
import sys
from time import time
from message_crypter import Message_crypter
from dotenv import load_dotenv
msg_crypt = Message_crypter()
load_dotenv()
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('gosling-pro.duckdns.org', 80)
# server_address = ('gosling-pro.duckdns.org', 80)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
# Leer historial del chat
cryto_key = msg_crypt.get_crypto_key('127.0.0.1')
if cryto_key == None:
    cryto_key = msg_crypt.generate_and_save_crypto_key('127.0.0.1')
log_file = open('../logs/chat_log.txt','r')
lines = log_file.readlines()
for line in lines:
    if len(line) > 1:
        print(msg_crypt.crypto_exec(line,msg_crypt.get_crypto_key('127.0.0.1'),0))
# try:
while True:
    # Send data
    message = input('Type a message: ')
    log_file = open('../logs/chat_log.txt','a')
    encrypted = msg_crypt.crypto_exec('<-- you say "{}"  ({})'.format(message,datetime.now()),cryto_key,1)
    log_file.write(encrypted+"\n")
    log_file.close()
    message = message.encode('utf-8')
    sock.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = 1024
    data = sock.recv(1024)
    amount_received += len(data)
    if amount_received > 0:
        encrypted = msg_crypt.crypto_exec('--> {} says "{}"  ({})'.format(server_address[0],data.decode('utf-8'),datetime.now()),cryto_key,1)
        log_file = open('../logs/chat_log.txt','a')
        log_file.write(encrypted+"\n")
        log_file.close()
        print('--> {} says {}  ({})'.format(server_address[0],data.decode('utf-8'),datetime.now()))
print('Socket closed')
sock.close()