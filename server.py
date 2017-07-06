#!/usr/bin/python
import socket
import sys
from main.gen_fun import fun_get

class SERVER(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('', 10021)
        #print >>sys.stderr, 'starting up on %s port %s' % self.server_address
        self.sock.bind(self.server_address)
        self.sock.listen(1)

    def loop_ever(self):
        while True:
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = self.sock.accept()
            try:
                len_read_str = connection.recv(4)

                if len_read_str != "0000":
                    len_read_int = int(len_read_str)
                    cmd = connection.recv(len_read_int)
                else:
                    cmd='help'
        
                response = fun_get(cmd).run()
                
                len_write_int = len(response)
                len_write_str = str(len_write_int).zfill(4)
                connection.send(len_write_str)
                connection.send(response)
        
            finally:
                # Clean up the connection
                connection.close()

if __name__=="__main__":
    server=SERVER()
    server.loop_ever()
