#server.py

import socket 
import threading

# connection details for the client

host = 'localhost' # host ip address
port = 12345

# server commencement

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# clients and their names
clients, nicknames = [], []

# handling statuses from the clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            try:
                print('{} left'.format(nickname).decode('utf-8'))
            except AttributeError:
                print('{} left'.format(nickname))
            nicknames.remove(nickname)
            break


# listening to clients
def receive():
    while True:
        # accepting the connection
        client, address = server.accept()
        print('Connected with {}'.format(str(address)))
        
        # request and store the nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        
        # printing the nickname
        print('Connected with {} at {}'.format(str(nickname), str(address)))
        client.send('Connected to server!'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
