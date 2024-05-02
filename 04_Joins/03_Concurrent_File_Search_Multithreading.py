import os
from threading import Thread, Lock

mutex = Lock()
matches = []

def file_search(root, filename):
    print("Searching in : ", root)
    directories = os.listdir(root)
    child_threads = []
    for file in directories:
        full_path = os.path.join(root, file)
        # print("file : ", file)
        # print("full_path : ", full_path)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if os.path.isdir(full_path):
            t = Thread(target=file_search, args=(full_path,filename))
            t.start()
            child_threads.append(t)
    for t in child_threads:
        t.join()
            

def main():

    root = "C:\\Users\\Victor\\Documents\\_ESTUDIOS\\Formation_Python\\09_Python_Parallel_Computing"
    filename = "README.md"

    t = Thread(target=file_search, args=(root,filename))
    t.start()
    t.join()
    if matches:
        for m in matches:
            print("Matched : ", m)
    else:
        print("No matches founded !")

main()