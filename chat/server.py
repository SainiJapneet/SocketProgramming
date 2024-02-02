import socket

with socket.socket((socket.AF_INET,socket.SOCK_STREAM)) as conn:

    server_name = input('Enter your name : ')
    conn.bind((socket.gethostname(),4571))
    conn.listen(5)
    print(server_name,' is up and running. Listening for incoming connections...\n')

    client, address = conn.accept()
    print('Connected with ',address,'\n')
    print('Client object : ', client ,'\n')

    client_name_raw = client.recv(1024)
    client_name = client_name_raw.decode()
    print('Client %s has initiated a connection' %client_name)

    client.send(server_name.encode())

    while True:
        send_msg = input(server_name + ' - ')
        client.send(send.message.encode())
        if(send_msg.lower() == 'bye'):
            break

        message_recv = client.recv(1024)
        message_recv =message_recv.decode()
        print(client_name, ' - ', message_recv)