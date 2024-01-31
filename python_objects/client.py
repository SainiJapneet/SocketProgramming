import socket
from product import Product
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.connect((socket,gethostname(),4571))
    while True:
        msg = conn.recv(1024)
        if not msg:
            print('No message from the server, Closing the connection...')
            break
        print('Message from server : ',msg.decode('utf-8'))
        print('Type of message received : ',type(msg))