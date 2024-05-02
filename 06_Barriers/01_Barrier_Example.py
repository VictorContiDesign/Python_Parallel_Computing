import time
from datetime import datetime
from threading import Barrier, Thread

barrier = Barrier(2)

def wait_on_barrier(name, time_to_sleep):
    for i in range(10):
        print(f"{name} is running : {datetime.now().time()}")
        time.sleep(time_to_sleep)
        print(f"{name} is waiting on the barrier : {datetime.now().time()}")
        barrier.wait()
            
    print(f"{name} is finished")
        
red = Thread(target=wait_on_barrier, args = ["red", 4])
blue = Thread(target=wait_on_barrier, args = ["blue", 10])

red.start()
blue.start()

time.sleep(8)
print("Barrier aborted")
barrier.abort()