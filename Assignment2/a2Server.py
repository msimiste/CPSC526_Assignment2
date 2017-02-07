
#!/usr/bin/python           # This is server.py file

#Name: Mike Simister
#StudentID: 10095107
#Tutorial Section: T02

import socket
import sys
import thread
import time
import socket               
import subprocess
import shlex
import os
import sys


def greeting():
    print "Port logger running: " +  sys.argv[1] + \
    " srcPort= " + sys.argv[2] \
     + " Host=" + sys.argv[3] \
     + " dstPort=" + sys.argv[4]

def main():
    #print(' '.join(str(x) for(x) in (sys.argv[1:])))
    greeting()
    testClient()
    
def testClient():
	host = sys.argv[3]
	port = int(sys.argv[2])
	data = 'GET / HTTP/1.1\r\n' + 'Host: ' + host + '\r\n\r\n'
	c = socket.socket()
	c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	c.connect((host,port))
	c.send(data)
	response = c.recv(4096)
	print response
if __name__ == '__main__':
    main()



