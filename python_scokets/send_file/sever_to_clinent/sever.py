



import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.172'
port = 50008
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):

        with open("data.txt","r") as data_to_send:
            r=data_to_send.read()

        self.sock.send(r.encode())

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
