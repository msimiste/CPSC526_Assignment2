
import socket
import sys
import threading
import time
import socket               
import subprocess
import shlex
import os
import sys
import errno
import itertools
import os
import re

def main():
    
   testClient()
    
    
def testClient():
    host = sys.argv[3]
    port = int(sys.argv[4])
    #data = 'GET / HTTP/1.1\r\n' + 'Host: ' + host + '\r\n\r\n'
    data = "Get"
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    c.connect((host,port))
    c.send(bytearray(data,'ascii'))
    print("line 17")
    response = c.recv(4096)
    print("line 19")
    print (response)
    c.close()
    
    
if __name__ == '__main__':
    main()
