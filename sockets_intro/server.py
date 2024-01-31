import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:#TCP socket intialization
    conn.bind((socket.gethostname(),4571))#binding socket with hostname and port number
    conn.settimeout(10)#server will wait for 10s for an incoming connection
    try:
        conn.listen(5)

        print('Server is up and running. Listening for incoming connections ...')

        client, address = conn.accept()#executed when a client accepts a connection
        print('Connection with ', address ,' established\n')
        print('Client object : ', client ,'\n')
        client.send(bytes('Hello, Welcome to socket programming','utf-8'))
    except socket.timeout:
        print('Timeout has been exceed. Closing the connection')