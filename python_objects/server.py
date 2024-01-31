import socket
from product import Product
import pickle
import time
#pickle is used for serialization/deserialization of python objects
#In serialization a python object is converted into a byte stream, vice versa for deserialization

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.bind((socket.gethostname(),4571))

    custom_objects = [Product('P024','Torch',100),
                      Product('P025','Keys',50),
                      Product('P026','RAM',500),
                      Product('P027','Mouse',150),
                      Product('P028','USB Cable',100)
                      ]

    conn.listen(2)
    print('Server is up and running. Listening for incoming connections...')

    client, address = conn.accept()
    print('Connection to ',address,' established\n')
    print('Client object : ',client,'\n')

    for product in custom_objects:
        pickled_product = pickle.dumps(product)
        client.send(pickled_product)
        print('Sent product : ',product.pid)
        time.sleep(2)
    #when we invoke the send function of a client we have send a byte object only