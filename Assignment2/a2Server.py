
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

BUFFER_SIZE = 4096
def greeting():
    print "Port logger running: " +  sys.argv[1] + \
    " srcPort= " + sys.argv[2] \
     + " Host=" + sys.argv[3] \
     + " dstPort=" + sys.argv[4]

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
   
   while True:
       s = socket.socket()             # Create a socket object
       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to make sure the connection doesn't hang
       sourceHost = sys.argv[3]          # Get local machine name
       print
       sourcePort = int(sys.argv[2]) 
       destPort = int(sys.argv[4])     # Reserve a port for your service.
       #print("line 51 : " + str(port)) 
       s.bind(('localhost', sourcePort))            # Bind to the port
       print("line 53 : " + str(sourcePort))
       testing = s.getsockname()
       print(str(testing[0]))
       s.listen(5)                     # Now wait for client connection.         
       c, addr = s.accept()        # Establish connection with client.
       c.send(bytearray("Testing12345"))
       print ('Got connection from', addr)
       #print("line 51 : " + str(port))
       thread.start_new_thread(listenToClient,(c,destPort))
       
       #print("Line 52")


#reference http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
def listenToClient(client, dPort):
    cont = True
    while cont:
        try:
            data = client.recv(BUFFER_SIZE, 0)
            while (len(data) == BUFFER_SIZE):
                data += client.recv(BUFFER_SIZE, 0)
           #data = data.decode("ascii")
            if(data == ''):
                #print("Client Closed")
                client.close()
            client.send(data)
            print("Line 72")
            data = data.decode('ascii')
            print(data)
        except socket.error as t:
            if t.errno == errno.EPIPE:
                print("Client Closed")
                cont = False
                client.send(bytearray("Broken Pipe"))
                client.close()
        except Exception, e:
             client.send(bytearray(str(e)+'\n', "ascii"))
       
             
    client.close()
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



