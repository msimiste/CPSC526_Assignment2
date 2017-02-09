import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 

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

#reference http://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
	def __init__(self,ip,port): 
		Thread.__init__(self) 
		self.ip = ip 
		self.port = port 
		print "[+] New server socket thread started for " + ip + ":" + str(port) 
	def run(self): 
	while True : 
		data = conn.recv(4096) 
		print "Server received data:", data
		MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
		if MESSAGE == 'exit':
			break
		conn.send(MESSAGE)  # echo

def main():
		
# Multithreaded Python server : TCP Server Socket Program Stub
	TCP_IP = get_ip() 
	TCP_PORT = 2004 
	BUFFER_SIZE = 20  # Usually 1024, but we need quick response 
	tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	tcpServer.bind((TCP_IP, TCP_PORT)) 
	threads = [] 
	destHost = sys.argv[3]
    server_address = destHost
    #print
    sourcePort = int(sys.argv[2]) 
    destPort = int(sys.argv[4])     # Reserve a port for your service.

	while True: 
		tcpServer.listen(4) 
		print "Multithreaded Python server : Waiting for connections from TCP clients..." 
		(conn, (ip,port)) = tcpServer.accept() 
		newthread = ClientThread(destHost,destPort) 
		newthread.start() 
		threads.append(newthread) 
	
	for t in threads: 
		t.join() 
