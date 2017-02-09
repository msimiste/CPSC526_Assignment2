
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
import errno
import itertools
import os
import re

BUFFER_SIZE = 4096
def greeting():
    print "Port logger running: " +  sys.argv[1] + \
    " srcPort= " + sys.argv[2] \
     + " Host=" + sys.argv[3] \
     + " dstPort=" + sys.argv[4]
     
#code for get_ip is modified from ----> http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
def get_ip():
    f = os.popen('ifconfig')
    for iface in [' '.join(i) for i in iter(lambda: list(itertools.takewhile(lambda l: not l.isspace(),f)), [])]:
        if re.findall('^(eth|wlan|em)[0-9]',iface) and re.findall('RUNNING',iface):
            ip = re.findall('(?<=inet )[0-9\.]+',iface)
            print(ip)
            if ip:
                return ip[0]
    return False
    
def main():
    #print(' '.join(str(x) for(x) in (sys.argv[1:])))
    greeting()
    #testClient()
    listenForClients()
    
    #listen
     #start thread    
    #if Connection
        #parse server/port info
        #connect to server
        #receive initial message from server
        #log initial response message
        #send initial response message to client
        #listen for messages 
        #send messages to server
        #log response message
        #send response message to client

def listenForClients():
    try:
        ip = get_ip()
        mainSock = socket.socket()
        mainSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sourcePort = int(sys.argv[2])
        destHost = sys.argv[3]
        destPort = int(sys.argv[4])
        mainSock.bind((ip, sourcePort))
        mainSock.listen(5)
        clientSock = mainSock.accept()[0]
        while True:            
            servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            servSock.connect((destHost,destPort))
            thread.start_new_thread(sendInfo, (clientSock, servSock))
            thread.start_new_thread(sendInfo, (servSock, clientSock))
    except Exception, e:
            print("Exception e =  " + str(e))
             #clientSock.send(bytearray(str(e)+'\n', "ascii"))
   # finally:
        #thread.start_new_thread(listenForClients,()) 
       

def sendInfo(sourceSocket, destinationSocket):
    data = 1 
    while data:
        data = sourceSocket.recv(BUFFER_SIZE)
        if(data):
            destinationSocket.sendall(data)
        else:
            #data = 0;
            sourceSocket.shutdown(socket.SHUT_RD)
            destinationSocket.shutdown(socket.SHUT_WR)

    
    

def testClient():
    host = sys.argv[3]
    port = int(sys.argv[4])
    data = 'GET / HTTP/1.1\r\n' + 'Host: ' + host + '\r\n\r\n'
    #data = "Get"
    c = socket.socket()
    c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    c.connect((host,port))
    c.send(data)
    response = c.recv(4096)
    print response
    c.send(data)
    response = c.recv(4096)
    print response
    c.close()
if __name__ == '__main__':
    main()




