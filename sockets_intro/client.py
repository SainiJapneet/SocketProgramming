import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((socket.gethostname(),4571))

    msg = conn.recv(1024)#1024 is the buffer size, It can receive 1024 bytes at a time
    print("Message from server : ", msg.decode,('utf-8'))
    