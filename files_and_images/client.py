import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.connect((socket.gethostname(),4571))

    '''
    custom_file = open('client_files/received_file.txt','wb')
    i = 1
    while True:
        data = conn.recv(40960)
        if not data:
            print('No message from the server. Closing the connection...')
            break
        custom_file.write(data)
        print('Batch ', i ,' of data written to file...')
        i += 1

    custom_file.close()
    '''

    with open('client_files/received_image.jpg','wb') as image_file:
        i = 1
        while True:
            data = conn.recv(40960)
            if not data:
                print('No message from the server. VClosing the connection...')
                break

            image_file.write(data)
            print('Batch ', i ,' of data written to file...')
            i += 1