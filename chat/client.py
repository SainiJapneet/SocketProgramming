import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    client_name = input('Enter your name : ')

    conn.connect((socket.gethostname(),4571))
    conn.send(client_name.encode())

    server_name_raw = conn.recv(1024)
    server_name = server_name_raw.decode()
    print('You have connected to the server %s'%server_name)

    while True:
         message_recv = conn.recv(1024)
         message_recv = message_recv.decode()
         print(server_name, ' - ', message_recv)

         send_msg = input(client_name + ' - ')
         conn.send(send_msg.encode())

         if send_msg.lower() == 'bye':
              break