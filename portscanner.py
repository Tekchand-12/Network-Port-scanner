import socket;import Queue
import threading;import warnings;from threading import Lock
import time;import termcolor
import sys
tester=[]
myset=[]


checkwarning=warnings.filterwarnings("ignore")
ip=raw_input("Enter the ip: ")
threads=raw_input("Enter the threads: ")
for i in range(0,5000):
    myset.append(i)

myset.sort()

def handler(m):
    handler=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        handler.settimeout(2)
        handler.connect((ip,m))
        if socket.getservbyport(m):
            sys.stdout.write("\rPort is open ===========================================> %s[%s]\n" % (m,socket.getservbyport(m)))
        else:
            sys.stdout.write("\rPort is Open ===========================================> %s[Unknown]\n" % (m))
        sys.stdout.flush()
        with open("ports.txt","a+") as fp:
            fp.write(m)

        sys.exit(1)
    except:
        sys.stdout.write("\rport is not open ==> %s" %(m))
        sys.stdout.flush()
    else:
        print "\n"
        print "[*]Complete"
if __name__ == "__main__":
    for oo in range(0,1):
        eventhandler=threading.Event()
        single=Lock()
        finisher=set()
        temp=[]
        for mm in range(0,65535):
            temp.append(mm)
        
        hacker=Queue.PriorityQueue(maxsize=len(temp))
    
        for mm in temp:
            hacker.put_nowait(int(mm))
    
        try:
            while hacker.empty() is not True:
                for i in range(0,int(threads)):
                    targets=threading.Thread(target=handler,args=(hacker.get_nowait(),))
                    finisher.add(targets)
                
                single.acquire()
                for p in finisher:
                    p.daemon=True
                    p.start()
                single.release()
                single.acquire()
                for o in finisher:
                    o.join()
                finisher.clear()
                single.release()
        except KeyboardInterrupt as qq:
            print termcolor.colored("[-] Operation Canceled by user","red",attrs=['bold'])
            pass
        except Exception as tt:
            print tt
            sys.exit(1)
