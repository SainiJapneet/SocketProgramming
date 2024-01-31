import socket
from product import Product
import pickle
#pickle is used for serialization/deserialization of python objects
#In serialization a python object is converted into a byte stream, vice versa for deserialization

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.bind((socket.gethostname(),4571))
    my_dictionary = {'a':1,'b':2}
    pickled_dictionary = pickle.dumps(my_dictionary)

    custom_object = Product('P024','Torch',100)
    pickled_object = pickle.dumps(custom_object)
    print('serialized dictionary type : ',type(pickled_dictionary))
    print('Serialized object type : ',type(pickled_object))
    conn.listen(2)
    print('Server is up and running. Listening for incoming connections...')

    client, address = conn.accept()
    print('Connection to ',address,' established\n')
    print('Client object : ',client,'\n')

    client.send(pickled_dictionary)
    client.send(pickled_object)
    #when we invoke the send function of a client we have send a byte object only