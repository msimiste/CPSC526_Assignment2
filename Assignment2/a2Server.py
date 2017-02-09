
#!/usr/bin/python           # This is server.py file

#Name: Mike Simister
#StudentID: 10095107
#Tutorial Section: T02

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


BUFFER_SIZE = 4096

    
def greeting():
    print ("Port logger running: " +  sys.argv[1] + \
    " srcPort= " + sys.argv[2] \
     + " Host=" + sys.argv[3] \
     + " dstPort=" + sys.argv[4])
     
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
   ip = get_ip()
   #print("ip: " + ip)
   while True:
       cSock = socket.socket()             # Create a socket object
       cSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to make sure the connection doesn't hang   
       
       #sourceHost = s.getsockname()
       #sourceHost = sourceHost[0]         # Get local machine ip
       #print("line 52, sourceHost = " + sourceHost)
       destHost = sys.argv[3]
       server_address = destHost
       #print
       sourcePort = int(sys.argv[2]) 
       destPort = int(sys.argv[4])     # Reserve a port for your service.
       #print("line 51 : " + str(port)) 
       cSock.bind((ip, sourcePort))            # Bind to the port
       #print("line 53 : " + str(sourcePort))
       #testing = s.getsockname()
       #print(str(testing[0]))       
       cSock.listen(5)                     # Now wait for client connection.         
       cli, addr = cSock.accept()        # Establish connection with client.
       cli.send(bytearray("Testing12345", 'ascii'))
       print ('Got connection from', addr)
       #print("line 51 : " + str(port))
       #sSock = socket.socket()  
       print("Socket Started")
       #sSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       #sSock.connect((destHost,destPort))
       threading.Thread(listenToClient(cli,destHost, destPort)).start()
       
       #print("Line 52")


#reference http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
def listenToClient(client,destHost,destPort):
    cont = True    
    print("Socket Started")        
    sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sSock.connect((destHost,destPort))
    sSock.connect((destHost,destPort))
    #sSock.setblocking(0)
    while cont:       
        try:                        
            data = client.recv(BUFFER_SIZE)
            while (len(data) == BUFFER_SIZE):
                data += client.recv(BUFFER_SIZE)
           #data = data.decode("ascii")
            if(data == ''):
                #print("Client Closed")
                client.close()
            #client.send(data)            
            sSock.sendall(data)
            data1 = ''
            print("Line 106")
            while 1:
				print("Line 117")
				servResp = sSock.recv(BUFFER_SIZE)
				print("Line 118")
				data1 += servResp
				print("Line 119")
				if not servResp:
					break				
            #sSock.sendto(data,(destHost,destPort))
            #servResp = sSock.recv(BUFFER_SIZE)
            #if(servResp != ""):
                #sSock.connect((destHost,destPort))
				#data1 = servResp
				#while(len(servResp) == BUFFER_SIZE):
					#servResp = sSock.recv(BUFFER_SIZE)
					#data1 += servResp
                #sSock.recv(BUFFER_SIZE)
            #print("Serv RespG: " + servResp)
            #while(len(servResp) == BUFFER_SIZE):
            #    servResp += serv.recv(BUFFER_SIZE,0)            
            client.send(data1)
            sSock.shutdown(socket.SHUT_RDWR)
            sSock.close()
            sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sSock.connect((destHost,destPort))
            #sSock.setblocking(0)
            #print("Line 72")
            #data = data.decode('ascii')
            #print(data)
        #except socket.error as t:
           # if t.errno == errno.EPIPE:
             #   print("Client Closed")
              #  cont = False
               # client.send(bytearray("Broken Pipe"))
                #client.close()
        except Exception as e:
             print("Exception e =  " + str(e))
             client.send(bytearray(str(e)+'\n', "ascii"))
       
             
    client.close()

def testClient():
    host = sys.argv[3]
    port = int(sys.argv[4])
    #data = 'GET / HTTP/1.1\r\n' + 'Host: ' + host + '\r\n\r\n'
    #data = "Get"
    c = socket.socket()
    c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    c.connect((host,port))
    c.send(data)
    response = c.recv(4096)
    print (response)
    c.close()
if __name__ == '__main__':
    main()




