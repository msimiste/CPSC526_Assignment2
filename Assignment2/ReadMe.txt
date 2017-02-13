Name: Mike Simister
StudentID: 10095107
Tutorial Section: T02

This program functions as a proxy on a linux machine.

To run the program:

(1) From the directory containing the assign1.py file:

	(1a)From cmd line type: python assign1.py (optional)<loggingFormat> <sourcePort) <host> <destPort>
		or for no logging format
	(1b)From cmd line type: python assign1.py <sourcePort) <host> <destPort>
	
	
(2)From the local machine or from another machine:
	
	(2a)From cmd line type: nc <host> <sourcePort> 
	(2b) If connecting to a netcat or ssh server via the proxy, the nc or ssh server must be initialized
	prior to sending a message from the client. That is, no connection will be made fromt the proxy, 
	until the client makes a connection and initiates communication.	
	

(3)Supported Logging Format:

Option			Description

				if no option is given the program will not display any logging

-raw 			All data will be logged as is, i.e. assumed to be ascii. Make sure to label each line of
				text with outgoing or incoming prefix (see examples).
-strip 			Similar to the -raw option, but only printable characters will be printed. Non-printable
				characters will be replaced with a dot ‘.’. Printable characters include whitespaces.
-hex 			All data will be logged in a format identical to the output of the linux ‘hexdump -C’
				utility. 
-autoN 			All data segments will be divided into N-byte long chunks, and each chunk will be
				displayed separately, on its own line. Each byte in the chunk will be displayed based
				on its value. If the byte is a backslash, tab, newline or carriage return, it’ll be reported
				in escaped form, i.e. ‘\\’, ‘\t’, ‘\n’ and ‘\r’ respectively. If the byte is in range 32..127, it
				will be displayed in raw form. In all other cases the byte will be displayed with a leading
				slash, followed by a two digit hexadecimal value of the byte.


(4)Known bugs:

	(4a)The program does NOT support tab-completion.
	
	
(5) Sample outputs for -raw,-hex,-strip,-autoN:


	
Sample -raw ouput - nc via proxy to http server(www.ucalgary.ca):


Proxy Server Side:

				[msimiste@zone08-ed Assignment2]$ python a2.py -raw 9999 www.ucalgary.ca 80
				Port logger running: -raw srcPort= 9999 Host=www.ucalgary.ca dstPort=80
				Listening
				('Got connection from', ('127.0.0.1', 41864))
				Socket Started
				('localhost', 9999)
				('www.ucalgary.ca', 80)

				
Logging info:


				---->GET /HTTP/1.1

				<----<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
				<----  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
				<----
				<----<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
				<----<head>
				<----  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
				<----
				<----  <title>404 - Page Not Found | University of Calgary</title>
				<----  
				<----  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
				<----  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
				....

Client Side: 

			msimiste@zone08-ed ~]$ nc localhost 9999
			GET /HTTP/1.1
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
			  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

			<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
			<head>
			  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

			  <title>404 - Page Not Found | University of Calgary</title>
			  
			  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
			  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
			  
			  <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>
			  ....

	
	
Sample -hex ouput - nc via proxy to http server(www.ucalgary.ca):

Proxy Server Side:

				
				[msimiste@zone08-ed Assignment2]$ python a2.py -hex 9999 www.ucalgary.ca 80
				Port logger running: -hex srcPort= 9999 Host=www.ucalgary.ca dstPort=80
				-hex
				Listening
				('Got connection from', ('127.0.0.1', 41920))
				Socket Started
				('localhost', 9999)
				('www.ucalgary.ca', 80)
				Listening

Logging info:
				----> 47 45 54 20 2f 48 54 54 50 2f 31 2e 31 0a   |GET /HTTP/1.1.|
				<---- 3c 21 44 4f 43 54 59 50 45 20 68 74 6d 6c 20 50   |<!DOCTYPE html P|
				<---- 55 42 4c 49 43 20 22 2d 2f 2f 57 33 43 2f 2f 44   |UBLIC "-//W3C//D|
				<---- 54 44 20 58 48 54 4d 4c 20 31 2e 30 20 53 74 72   |TD XHTML 1.0 Str|
				<---- 69 63 74 2f 2f 45 4e 22 0a 20 20 22 68 74 74 70   |ict//EN".  "http|
				<---- 3a 2f 2f 77 77 77 2e 77 33 2e 6f 72 67 2f 54 52   |://www.w3.org/TR|
				<---- 2f 78 68 74 6d 6c 31 2f 44 54 44 2f 78 68 74 6d   |/xhtml1/DTD/xhtm|
				<---- 6c 31 2d 73 74 72 69 63 74 2e 64 74 64 22 3e 0a   |l1-strict.dtd">.|
				<---- 0a 3c 68 74 6d 6c 20 78 6d 6c 6e 73 3d 22 68 74   |.<html xmlns="ht|
				<---- 74 70 3a 2f 2f 77 77 77 2e 77 33 2e 6f 72 67 2f   |tp://www.w3.org/|
				<---- 31 39 39 39 2f 78 68 74 6d 6c 22 20 78 6d 6c 3a   |1999/xhtml" xml:|
				<---- 6c 61 6e 67 3d 22 65 6e 22 20 6c 61 6e 67 3d 22   |lang="en" lang="|
				<---- 65 6e 22 3e 0a 3c 68 65 61 64 3e 0a 20 20 3c 6d   |en">.<head>.  <m|
				<---- 65 74 61 20 68 74 74 70 2d 65 71 75 69 76 3d 22   |eta http-equiv="|
				<---- 43 6f 6e 74 65 6e 74 2d 54 79 70 65 22 20 63 6f   |Content-Type" co|
				<---- 6e 74 65 6e 74 3d 22 74 65 78 74 2f 68 74 6d 6c   |ntent="text/html|
				<---- 3b 20 63 68 61 72 73 65 74 3d 75 74 66 2d 38 22   |; charset=utf-8"|
				<---- 2f 3e 0a 0a 20 20 3c 74 69 74 6c 65 3e 34 30 34   |/>..  <title>404|
				<---- 20 2d 20 50 61 67 65 20 4e 6f 74 20 46 6f 75 6e   | - Page Not Foun|
				....
				
Client Side: 

			msimiste@zone08-ed ~]$ nc localhost 9999
			GET /HTTP/1.1
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
			  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

			<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
			<head>
			  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

			  <title>404 - Page Not Found | University of Calgary</title>
			  
			  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
			  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
			  
			  <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>
			  ....



Sample -strip ouput - nc via proxy to http server(www.ucalgary.ca):

Proxy Server Side:

				[msimiste@zone08-ed Assignment2]$ python a2.py -strip 9999 www.ucalgary.ca 80
				Port logger running: -strip srcPort= 9999 Host=www.ucalgary.ca dstPort=80
				Listening
				('Got connection from', ('127.0.0.1', 41954))
				Socket Started
				('localhost', 9999)
				('www.ucalgary.ca', 80)
				Listening

				
Logging info:


				---->GET /HTTP/1.1
				
				<----<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
				<----  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
				<----
				<----<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
				<----<head>
				<----  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
				<----
				<----  <title>404 - Page Not Found | University of Calgary</title>
				<----  
				<----  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
				<----  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
				<----  
				<----  <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>
				<----  <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/modernizr/modernizr.svg.js"></script>
				<----  <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/svg-png-polyfill/svgpng.js"></script>
				....

				
Client Side: 

			msimiste@zone08-ed ~]$ nc localhost 9999
			GET /HTTP/1.1
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
			  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

			<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
			<head>
			  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

			  <title>404 - Page Not Found | University of Calgary</title>
			  
			  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
			  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
			  
			  <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>
			  ....

Sample -autoN(n=8) ouput - nc via proxy to http server(www.ucalgary.ca):

Proxy Server Side:

				[msimiste@zone08-ed Assignment2]$ python a2.py -auto8 9999 www.ucalgary.ca 80
				Port logger running: -auto8 srcPort= 9999 Host=www.ucalgary.ca dstPort=80
				Listening
				('Got connection from', ('127.0.0.1', 41962))
				Socket Started
				('localhost', 9999)
				('www.ucalgary.ca', 80)
				Listening

Logging Info

				---->GET
				----> /HTTP/1
				---->.1'\n'
				<----<!D
				<----OCTYPE h
				<----tml PUBL
				<----IC "-//W
				<----3C//DTD 
				<----XHTML 1.
				<----0 Strict
				<----//EN"'\n'  
				<----"http://
				<----www.w3.o
				<----rg/TR/xh
				<----tml1/DTD
				<----/xhtml1-
				<----strict.d
				<----td">'\n''\n'<h
				<----tml xmln
				<----s="http:
				<----//www.w3
				<----.org/199
				<----9/xhtml"
				<---- xml:lan
				<----g="en" l
				<----ang="en"
				<---->'\n'<head>
				<----'\n'  <meta
				<---- http-e
				....
				
Client Side: 

			msimiste@zone08-ed ~]$ nc localhost 9999
			GET /HTTP/1.1
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
			  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

			<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
			<head>
			  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

			  <title>404 - Page Not Found | University of Calgary</title>
			  
			  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
			  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
			  
			  <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>	
			  ....
