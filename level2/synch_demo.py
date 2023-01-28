from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("good evening",end=' ')
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=('sahithi',))
t2=Thread(target=wish,args=('mini',))
t3=Thread(target=wish,args=('mart',))
t1.start()
t2.start()
t3.start()