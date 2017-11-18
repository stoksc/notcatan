import socket
import sys
from time import clock


class ClientControl():
    def __init__(self):
        #create a tcp/ip socket
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        #connect the socket to the port where the server is listening
        serv_addr = ('localhost', 8000)
        print('connecting to {} port {}'.format(serv_addr[0],serv_addr[1]))
        self.sock.connect(serv_addr)

    def send_build_obj(self):
        #send data
        thing, tile, number = input("thing: "), input("tile: "), input("number: ")
        msg = thing + tile + number
        byte_msg = msg.encode('utf-8')
        self.sock.sendall(byte_msg)

    def close(self):
        print("closing socket")
        self.sock.close()
        print("closing application")

if __name__ == '__main__':
    c = ClientControl()
    while input('more? ') != 'no':
        c.send_build_obj()
    c.close()
    quit()
