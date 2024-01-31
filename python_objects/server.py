import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.bind((socket.gethostname(),4571))
    my_dictionary = {'a':1,'b':2}
    custom_object = Product('P024','Torch',100)
    conn.listen(2)
    print('Server is up and running. Listening for incoming connections...')

    client, address = conn.accept()
    print('Connection to ',address,' established\n')
    print('Client object : ',client,'\n')

    client.send(bytes(str(my_dictionary),'utf-8'))
    client.send(bytes(str(custom_object),'utf-8'))