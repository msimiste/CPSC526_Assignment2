
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
STRIP = False
HEX = False
AUTON = False
RAW = False
_STRIP_ = '-strip'
HEX_STR = '-hex'
_AUTO_N = '-auto'
N_VALUE = ''

    
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
   def __init__ ( self, channel, details, receiver, threads, prefix ):

      self.channel = channel
      self.details = details
      self.receiver = receiver
      self.threads = threads
      self.prefix = prefix
      threading.Thread.__init__ ( self )

   def run ( self ):
        cont = True
        print(self.details)
        try:
            while cont:                                     
                servResp = self.channel.recv(BUFFER_SIZE)
                #servResp = 
                self.receiver.send(servResp)
                logging(servResp, self.prefix)
                #print(logged)      
                if not servResp:
                    print(str(self.details) + ": line 66")
                    self.receiver.close()
                    self.channel.close()
                    #os.unlink(self.details[1])
                    cont = False                    
                                                          
        except socket.error as t:
            if t.errno == errno.EPIPE:
                print("Client Closed")
                cont = False
                self.receiver.send(bytearray("Broken Pipe"))
                #self.receiver.close()
                #self.channel.close()
                        
   
def main():
    #print(' '.join(str(x) for(x) in (sys.argv[1:])))
    #greeting()
    #testClient()
    setParseParams()
    print("line97")
    listenForClients()    

def logging(inputVal, prefix):
    #logged = inputVal.split('\n')
    #print logged
    
    #logged  = map(lambda c: hex(ord(c)),inputVal)
    #print type(logged')
    #logged[0] = '---->' + logged[0]
    #print (prefix + logged[0] + '\n')
    #temp = prefix.join((x) for x in logged )
    #temp = prefix + temp
    #print temp
    #print("Raw = : "+ str(RAW))
    #print("Hex = : "+ str(HEX))
    #print("strip = : "+ str(STRIP))
    #print("auton = : "+ str(AUTON))
    if(RAW):
        pre = prefixToOrds(prefix)
        merged = inputToOrds(pre,inputVal) 
        merged = _raw(pre,merged)
        print(merged)
    elif(HEX):
        #merged = map(lambda c: hex(ord(c)),inputVal)
        #merged = ' '.join(x[2:] for x in merged)
        #merged = re.findall('........', inputVal)
        merged = [inputVal[i:i+8]  for i in range(0, len(inputVal), 8)]
        merged2 = [inputVal[i:i+16]  for i in range(0, len(inputVal), 16)]
        hexed =  map(lambda h: convertHex(h), merged)
        #test = map(lambda h: h + '  ' , hexed)   
        #merged2 = map(lambda h: '|'+ h + '|' , merged2)
        #merged = map(lambda g: merged[g] + merged[g+1], merged)
       # merged = [merged[i:i+2] for i in range(0, len(merged), 2)]         
        test =   [hexed[i:i+2] for i in range(0, len(hexed), 2)] 
        temp = zip(test,merged2)
        #print(temp)
        for h,t in zip(test,merged2):
          	print ' '.join(h[0][0:][0:]),'|',(t),'|'
            #print('|')
            #print(merged[i])
            #print('|\n')
        #test = [test[i]  merged[i] for i in range(0,len(test), 1)]
        #test  =  [merged.insert(i,'  ') for i in range(1, len(merged), 1)]
        #hexed = [hexed[i:i+2] for i in range(0,len(hexed),2)]
        #hexed = map(lambda x: (x[0] + x[1]), hexed)
        #testing = _HexDmp(hexed,merged)
        #print(merged2)
        #print(hexed)
        #print /H("Logging: 109")
        #print type(inputVal)        
    elif(STRIP):
        #print type("Logging: 112")
        pre = prefixToOrds(prefix)
        merged = inputToOrds(pre,inputVal)
        merged = _Strip(pre,merged) 
        #question for TA, do we want to include newline chars?
        merged = merged.replace('.', '.\n')
        #print (merged)         
    elif(AUTON):
        print type(inputVal)
        print type("Logging: 116")  
    #else:
       # raise Exception("Logging Format Error no value given")
    #return logged

def inputToOrds(prefix,inputVal):
    rawLog = map(lambda c: ord(c), inputVal)
    #pre = prefixToOrds(prefix)
    merged = prefix + rawLog    
    return merged

def prefixToOrds(prefix):
    pre = map(lambda c: ord(c), prefix) 
    return pre
             
def _raw(prefix,inVal):
    outVal = insertPrefix(inVal,prefix)
    outVal = ''.join(str(chr(x)) for x in outVal)
    return outVal

def _Strip(prefix,inVal):
    outVal = insertPrefix(inVal,prefix)
    outVal = ''.join(str(chr(convertPrintable(x))) for x in outVal)
    return outVal

def convertPrintable(inOrd):
    if((inOrd < 32) or(inOrd > 127)):
        return  46
    else:
        return inOrd
    #elif(inOrd > 127)
    #   return 46
def convertHex(inVal):
    merged = map(lambda c: hex(ord(c))[2:],inVal)
    for x,v in enumerate(merged):
	   if len(v) < 2:
		  merged[x] = '0' + v
    #print(merged)
    #outVal = ' '.join(x[2:] for x in merged)
    return merged       

def _HexDmp(list1, list2):
    n = 2
    #hexList = [list1[i:i+n] for i in range(0, len(list1), n)]
    #strList = [list2[i:i+n] for i in range(0, len(list2), n)]
    #zippedList = zip(hexList,strList)
    #zippedList = map(lambda x: x[0][0:] + '  ' + x[0][1] + '  |' + x[1][0] + x[1][1] +'|', zippedList)
    #print(zippedList)
    #return output

#def autoN():

def insertPrefix(inputList, prefix):
    prefix.reverse()
    end = len(inputList)
    for i,v in enumerate(inputList):
       if (v == 10 and i != end-1):
           #print(i,v)
           map(lambda x: inputList.insert(i+1,x), prefix)    
    return inputList 
    
def setParseParams():
    print("line 128")
    try:
        arg = sys.argv[1] 
        print("Argv: " + str(arg))
        print(str(str(arg).upper()[0:4] == HEX_STR.upper()))
        print(str(arg).upper()[0:4])
        print(HEX_STR.upper())  
        if (str(arg).upper()[0:4] == HEX_STR.upper()):
            print("parse 106" + str(arg))
            print(arg[0:4])
            global HEX
            HEX = True
        elif(str(arg).upper()[0:4] == '-raw'.upper()):
            print("parse 141" + str(arg))
            global RAW 
            RAW = True
        elif (str(arg).upper()[0:5] == _AUTO_N.upper()):
            print("parse 109" + str(arg))
            print(arg[0:5])
            global AUTON
            AUTON = True
            global N_VALUE
            N_VALUE = int(arg[5:]) 
            print("NVAL = " + str(N_VALUE))         
        elif(str(arg).upper()[0:6] == _STRIP_.upper()):
            print("parse 113" + str(arg))
            print(arg[0:6])
            global  STRIP
            STRIP = True
        #else:
            #raise Exception("Bad Flag Choice")
    except Exception as e:
        print("Exception: " + str(e))   

def listenForClients():
   ip = 'localhost'
   #ip = get_ip()
   #ip = '68.145.126.231'
   #print("ip: " + ip)  
   cSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)             # Create a socket object
   cSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to make sure the connection doesn't hang   
   if(len(sys.argv) == 5):
       destHost = sys.argv[3]         
       sourcePort = int(sys.argv[2]) 
       destPort = int(sys.argv[4])     # Reserve a port for your service.     
   else:
       destHost = sys.argv[2]         
       sourcePort = int(sys.argv[1]) 
       destPort = int(sys.argv[3])       
   cSock.bind(('', sourcePort))            # Bind to the port
   cSock.listen(5) # Now wait for client connection.                                
   threads = []    
   while True:
      print("Listening")  
      cli, addr = cSock.accept()       # Establish connection with client. 
      print("line106")         
      sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print("line108")
      sSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
      sSock.connect((destHost,destPort))
      sSock.send('')
      print ('Got connection from', addr)       # 
      print("Socket Started")      
      try:
         cThread = ClientThread(cli, (ip, sourcePort),sSock, threads, '<----')
         cThread.start()
         threads.append(cThread)
         sThread = ClientThread(sSock, (destHost,destPort),cli, threads,'---->')
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




