import time
from threading import Thread

def child_1():
    print("Child 1 Thread doing work...")
    time.sleep(5)
    print("Child 1 Thread done...")
    
def child_2():
    print("Child 2 Thread doing work...")
    time.sleep(5)
    print("Child 2 Thread done...")
       
def parent():
    t1 = Thread(target=child_1, args=())
    t1.start()
    t2 = Thread(target=child_2, args=())
    t2.start()
    print("Parent Thread is waiting...")
    t1.join()
    t2.join()
    print("Parent Thread is unblocked...")
    
parent()