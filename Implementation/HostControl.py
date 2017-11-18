import socket
import sys
import queue
import os
import time
import threading
from multiprocessing import Pool
import Constants

NUMBER_OF_CLIENTS = Constants.NUMBER_OF_CLIENTS

class HostControl:
    def __init__(self, serv_addr):
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        print('starting up on {} port {}'.format(serv_addr[0],serv_addr[1]),
              file=sys.stderr)
        self.sock.bind(serv_addr)
        self.sock.listen()
        self.clients = []
        self.processes = []
        self.requests = queue.Queue()

    def get_conns(self):
        while True:
            print('{} connections. \nwaiting for more'.format(len(self.clients)),
                file=sys.stderr)
            self.client = self.connection, self.client_addr = self.sock.accept()
            self.clients.append(self.client)
            t = threading.Thread(target=self.rec_data, args=(self.client,))
            t.start()
            if len(self.clients) == NUMBER_OF_CLIENTS:
                print('{} clients connected. done.'.format(NUMBER_OF_CLIENTS))
                break
        return self.clients
    
    def rec_data(self, client):
        while 1:
            time.sleep(1)
            data = bytes.decode(client[0].recv(128))
            request = (client, data)
            self.requests.put(request)

    def close(self):
        print('closing socket')
        self.sock.close()
