# client.py

import socket
import threading
import sys

nickname = input("Enter your nickname:")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',12345)) # host ip address

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        message = '{} : {}'.format(nickname, input())
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
