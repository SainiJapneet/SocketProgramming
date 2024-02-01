import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.connect((socket.gethostname(),4571))

    custom_file = open('client_files/received_file.txt','wb')
    while True:
        data = conn.recv(40960)
        if not data:
            print('No message from the serve. Closing the connection...')
            break
        custom_file.write(data)
        print('Batch of data written to file...')

    custom_file.close