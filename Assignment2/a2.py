
#!/usr/bin/python           # This is server.py file

#Name: Mike Simister
#StudentID: 10095107
#Tutorial Section: T02

import socket
import sys
import threading
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


#reference http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/
# Our thread class:
class ClientThread ( threading.Thread):

   # Override Thread's __init__ method to accept the parameters needed:
   def __init__ ( self, channel, details, receiver, threads ):

      self.channel = channel
      self.details = details
      self.receiver = receiver
      self.threads = threads
      threading.Thread.__init__ ( self )

   def run ( self ):
        cont = True
        print(self.details)
        try:
            while cont:                                     
                servResp = self.channel.recv(BUFFER_SIZE)
                self.receiver.send(servResp)      
                if not servResp:
                    print(str(self.details) + ": line 66")
                    #self.receiver.send('')
                    self.receiver.close()
                    self.channel.close()
                    #self.receiver.join()
                    for t in self.threads[1:]:
                        t.join()
                    cont = False                    
                    # Exception('You need to enter a value')                                      
        except socket.error as t:
            if t.errno == errno.EPIPE:
                print("Client Closed")
                cont = False
                self.receiver.send(bytearray("Broken Pipe"))
                #self.receiver.close()
                #self.channel.close()
                        
   
def main():
    #print(' '.join(str(x) for(x) in (sys.argv[1:])))
    greeting()
    #testClient()
    listenForClients()    
   

def listenForClients():
   #ip = 'localhost'
   ip = get_ip()
   #ip = '10.13.168.192'
   #print("ip: " + ip)  
   cSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)             # Create a socket object
   cSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to make sure the connection doesn't hang   
   destHost = sys.argv[3]         
   sourcePort = int(sys.argv[2]) 
   destPort = int(sys.argv[4])     # Reserve a port for your service.     
   cSock.bind(('', sourcePort))            # Bind to the port
   cSock.listen(5) # Now wait for client connection.                                
   threads = []    
   while True:
      print("Listening")  
      cli, addr = cSock.accept()       # Establish connection with client. 
      print("line106")         
      sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print("line108")
      #sSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
      sSock.connect((destHost,destPort))
      sSock.send('')
      print ('Got connection from', addr)       # 
      print("Socket Started")      
      try:
         cThread = ClientThread(cli, (ip, sourcePort),sSock, threads)
         cThread.start()
         threads.append(cThread)
         sThread = ClientThread(sSock, (destHost,destPort),cli, threads)
         sThread.start()
         threads.append(sThread)
      except Exception as b:
          print("Exception b =" + str(b))
          sSock.close()
          #break             
      #finally:
        #  thread.start_new_thread(listenForClients,()) 
        



if __name__ == '__main__':
    main()




