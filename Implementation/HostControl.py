'''
Class wraps all the socket stuff for the Host to use.
'''

import socket
import sys
import queue
import os
import time
import threading
import Constants

NUMBER_OF_CLIENTS = Constants.NUMBER_OF_CLIENTS

class HostControl:
    def __init__(self, serv_addr):
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        print('starting up on {} port {}'.format(serv_addr[0],serv_addr[1]))
        self.sock.bind(serv_addr)
        self.sock.listen()
        self.clients = []
        self.requests = queue.Queue()

    def get_conns(self):
        '''
        Listens for connects and returns a list of (active_conns, addrs) when it has NUMBER_OF_CLIENTS connections.

        Args:
            None
        Returns:
            [(Socket, ip_addr)]
        '''
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
        '''
        Receives and decodes data and puts it on a request queue.

        Args:
            None
        Returns:
            None
        '''
        while 1:
            time.sleep(1)
            data = bytes.decode(client[0].recv(128))
            request = (client, data)
            self.requests.put(request)

    def send_data(self, connection, message):
        '''
        Sends '|' + message encoded as utf-8 to the connection passed. ('|' solves client receives clumps of request when they come in too fast)

        Args:
            Socket, String
        Returns:
            None
        '''
        connection.send(('|'+message).encode('utf-8'))

    def close(self):
        '''
        Close the host connection.

        Args:
            None
        Returns:
            None
        '''
        print('closing socket')
        self.sock.close()
