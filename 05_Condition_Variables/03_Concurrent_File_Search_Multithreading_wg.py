import os
from threading import Thread, Lock
from _02_Wait_Group import WaitGroup

mutex = Lock()
matches = []

def file_search(root, filename, wait_group):
    print("Searching in : ", root)
    directories = os.listdir(root)
    for file in directories:
        full_path = os.path.join(root, file)
        # print("file : ", file)
        # print("full_path : ", full_path)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if os.path.isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=(full_path,filename, wait_group))
            t.start()
    wait_group.done()
            

def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    root = "C:\\Users\\Victor\\Documents\\_ESTUDIOS\\Formation_Python\\09_Python_Parallel_Computing"
    filename = "README.md"

    t = Thread(target=file_search, args=(root,filename, wait_group))
    t.start()
    wait_group.wait()
    if matches:
        for m in matches:
            print("Matched : ", m)
    else:
        print("No matches founded !")

main()