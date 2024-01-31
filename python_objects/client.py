import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.connect((socket.gethostname(),4571))
    while True:
        msg = conn.recv(1024)
        if not msg:
            print('No message from the server, Closing the connection...')
            break
        
        print('Type of message received : ',type(msg))
        print('Message data : ',msg)
        unpickled_msg = pickle.loads(msg)
        print('Type of deserialized message : ',type(unpickled_msg))
        print('Deserialized message data : ',unpickled_msg)