from threading import *
import time
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print("good evening",end=' ')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('sahithi',))
t2=Thread(target=wish,args=('mini',))
t3=Thread(target=wish,args=('mart',))
t4=Thread(target=wish,args=('box',))
t5=Thread(target=wish,args=('pen',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


