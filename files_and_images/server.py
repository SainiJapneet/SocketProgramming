import socket
from PIL import Image
#PIL is Python imaging Library used to open/manipulate and perform other operations on an image
#socket.AF_INET specifies that we are going to attach the socket to address specified by hostname and socket number
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.bind((socket.gethostname(),4571))
    conn.listen(5)
    print('Server is up and running. Listening for connection...\n')

    client, address = conn.accept()
    print('Connection to : ',address,' established\n')
    print('Client object : ',client,'\n')

    '''
    custom_file = open('server_files/pg10.txt','rb')#rb is used to specify that we are opening file in read only mode and in binary format
    
    custom_data = custom_file.read(40960)# we will read 40Kb of data in a go.
    while(custom_data):
        client.send(custom_data)
        custom_data = custom_file.read(40960)
    print('Custom file sent successfully')
    '''

    with open('server_files/demo_img.jpg','rb') as image_file:
        image_batch = image_file.read(40960)
        i = 1
        while(image_batch):
            client.send(image_batch)
            image_batch = image_file.read(40960)
            print('Batch ', i ,'sent to client...')
            i += 1
print('Image sent successfully')
