import os
from threading import Thread

matches = []

def file_search(root, filename):
    print("Searching in : ", root)
    directories = os.listdir(root)
    for file in directories:
        full_path = os.path.join(root, file)
        # print("file : ", file)
        # print("full_path : ", full_path)
        if filename in file:
            matches.append(full_path)
        if os.path.isdir(full_path):
            file_search(full_path, filename)
                       

def main():

    root = "C:\\Users\\Victor\\Documents\\_ESTUDIOS\\Formation_Python\\09_Python_Parallel_Computing"
    filename = "README.md"

    file_search(root, filename)
    if matches:
        for m in matches:
            print("Matched : ", m)
    else:
        print("No matches founded !")

main()