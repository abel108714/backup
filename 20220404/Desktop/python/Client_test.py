import os
import socket

HOST = '172.21.7.39'#'127.0.0.1''172.21.7.39'
PORT = 8000
clientMessage = 'Hello!'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(clientMessage.encode())

serverMessage = str(client.recv(1024), encoding='utf-8')
print('Server:', serverMessage)

client.close()

os.system("pause")