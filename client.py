#!/usr/bin/python
import socket
import sys
import time
# Create a TCP/IP socket
class CLIENT(object):
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def reader(self):
        #try:
            len_read_str = self.sock.recv(4)
            len_read_int = int(len_read_str)
            data = self.sock.recv(len_read_int)
            return data

    def writer(self,data):
        try:
            len_write_int = len(data)
            len_write_str = str(len_write_int).zfill(4)
            self.sock.send(len_write_str)
            self.sock.sendall(data)
            return 0

        except:
            return -1


    def close(self):
        self.sock.close()

def main():
    client = CLIENT()
    client.connect('localhost', 10021)
    try:
        cmd = sys.argv[1]
    except IndexError:
        cmd = ""
        
    client.writer(cmd)
    response = client.reader()
    client.close()
    print >>sys.stderr, response
    
if __name__=="__main__":
    main()
