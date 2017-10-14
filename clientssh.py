#! python3
from socket import *
import sys
servername="192.168.56.103"
sport=12003
csock=socket(AF_INET,SOCK_STREAM)
csock.connect((servername,sport))
cmd=input("Enter cmd")
while cmd!="exit":
    csock.send(cmd.encode())
    cont=csock.recv(2048)
    print(cont.decode())
    cmd=input("Enter cmd")
    if cmd=="exit":
        break;
csock.close()

if(cmd=="exit"):
    csock.close()
    sys.exit()
