#!/bin/python
import sys
import socket
from datetime import datetime as time

#Define target
if (len(sys.argv))==2:
    target=socket.gethostbyname(sys.argv[1])
else:
    print("Incorrect Syntax / Number of arguments")
    print("Syntax: python3 portscanner.py <ip> ")
	
#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(time.now()))
print("-" * 50)
print("PORT SCANNER IS SCANNING ")
print(time.now())
print("-" * 50)

#Scanning method
try:
    for port in range(1,65535):
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
