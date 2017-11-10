import socket
import sys
import queue
import os
import queue
import time
from multiprocessing import Pool

NUMBER_OF_CLIENTS = 6

class ServerControl:
    def __init__(self, serv_addr):
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        print('starting up on {} port {}'.format(serv_addr[0],serv_addr[1]),
              file=sys.stderr)
        self.sock.bind(serv_addr)
        self.sock.listen()
        self.clients = []
        self.processes = []

    def get_conns(self):
        while True:
            print('{} connections. \nwaiting for more'.format(len(self.clients)),
                file=sys.stderr)
            self.client = self.connection, self.client_addr = self.sock.accept()
            self.clients.append(self.client)
            if len(self.clients) == NUMBER_OF_CLIENTS:
                print('{} clients connected. done.'.format(NUMBER_OF_CLIENTS))
                print(self.clients)
                break

    def manage_conns(self):
        with Pool(NUMBER_OF_CLIENTS) as p:
            p.map(self.rec_data, self.clients)

    def rec_data(self, client):
        while 1:
            time.sleep(1)
            data = bytes.decode(client[0].recv(128))
            print(data)

    def close(self):
        print('closing socket')
        self.sock.close()

if __name__ == '__main__':
    serv_addr = ('localhost', 5000)
    s = ServerControl(serv_addr)
    s.get_conns()
    s.manage_conns()
    s.close()
    quit()
