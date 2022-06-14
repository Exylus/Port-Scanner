#!/bin/python
import sys
import socket
from datetime import datetime as time

#Define target
if (len(sys.argv))==4:
    target=socket.gethostbyname(sys.argv[1])
    minPort=(int(sys.argv[2]))
    maxPort=(int(sys.argv[3]))
else:
	print("-" * 50)
	print("Incorrect Syntax")
	print("Syntax: ./portscanner.py <ip> <min_port> <max_port>")
	print("-" * 50)
	sys.exit()
	
#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(time.now()))
print("-" * 50)
print("PORT SCANNER IS SCANNING ON RANGE "+str(minPort)+"-"+str(maxPort))
print(time.now())
print("-" * 50)
#Scanning method
if (minPort < 1 or minPort > maxPort or maxPort > 65535):
	print "Incorrect port Syntax"
	print "- ports must be between 1 & 65535"
	print "- maxPort must be greater or equal to minPort"
	print("-" * 50)
else:
	try:
		for port in range(minPort,maxPort):
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result=s.connect_ex((target,port))
			if result==0:
				print("port {} is open".format(port))
			s.close()
	#System Exits
	except KeyboardInterrupt:
		print("Exiting script")
    		sys.exit()
	except socket.gaierror:
	  	print("Host Name Could not be Resolved")
	    	sys.exit()
	except socket.error:
	    	print("Couldnt connect to server")
	    	sys.exit()	
	

