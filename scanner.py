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


try:
    for port in range(1,65535):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        print(port)
        if result==0:
            print("The %d is open"%(port))
        s.close()

