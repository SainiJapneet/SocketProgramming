import socket

#socket.AF_INET specifies that we are going to attcah the socket to address specified by hostname and socket number
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.bind((socket.gethostname(),4571))
    conn.listen(5)
    print('Server is up and running. Listening for connection...\n')

    client, address = conn.accept()
    print('Connection to : ',address,' established\n')
    print('Client object : ',client,'\n')
    custom_file = open('server_files/archive/pg10.txt','rb')#rb is used to specify that we are opening file in read only mode and in binary format
    
    custom_data = custom_file.read(40960)# we will read 40Kb of data in a go.
    while(custom_data):
        client.send(custom_data)
        custom_data = custom_file.read(40960)
    print('Custom file sent successfully')