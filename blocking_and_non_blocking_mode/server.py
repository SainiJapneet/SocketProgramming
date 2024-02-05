from datetime import datetime
import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:

    conn.bind((socket.gethostname(),4571))
    conn.listen(5)
    print('Server is up and running. Listening for connections...\n')

    client, address = conn.accept()
    print('Connection to ',address,' established\n')
    print('Connected to ',client,'\n')
