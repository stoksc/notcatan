import socket
import sys
from time import clock
import threading
import queue


class ClientControl():
    def __init__(self):
        #create a tcp/ip socket
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        #connect the socket to the port where the server is listening
        serv_addr = ('localhost', 8000)
        print('connecting to {} port {}'.format(serv_addr[0],serv_addr[1]))
        self.sock.connect(serv_addr)
        self.requests = queue.Queue()
        threading.Thread(target=self.rec_data, args=()).start()

    def send_build_obj(self, msg):
        #send data
        byte_msg = msg.encode('utf-8')
        self.sock.sendall(byte_msg)

    def rec_data(self):
        while True:
            self.requests.put(self.sock.recv(1024).decode('utf-8'))

    def close(self):
        print("closing socket")
        self.sock.close()
        print("closing application")

if __name__ == '__main__':
    c = ClientControl()
    def handle_send():
        while True:
            while not c.requests.empty():
                current_requests = c.requests.get().split('|')
                for req in current_requests:
                    if req == '':
                        pass
                    elif req[0:4] == 'sett':
                        print('build a settlement')
                    elif req[0:4] == 'road':
                        print('build a road')
                    elif req[0:4] == 'rsrc':
                        print('resources: ', end='')
                        print(req[4::].split(' '))
                    elif req[0:4] == 'strt':
                        print('starting turn')
                    elif req[0:4] == 'endt':
                        print('ending turn')
                    elif req[0:4] == 'errr':
                        print('last build attempt failed')
                    elif req[0:4] == 'roll':
                        print('rolled a ' + req[4])
                    else:
                        print('unhandled return')
                        print(req)
            while input('more? ') != 'no':
                msg = input('msg: ')
                c.send_build_obj(msg)
    r = threading.Thread(target=handle_send, args=())
    r.start()
    # c.close()
    # quit()
