import os
from sys import *

def Checkfile(file_Name):
    f = open(file_Name,"r")
    print("create a new file")
    new_file = input()
    f1 = open(new_file, "w")
    for elem in f:
        f1.write(elem)

def main():
    print("Application started")
    print("Application Name",argv[0])

    if len(argv) < 2:
        print("Insufficient Argument:")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This script is used to check file is exist or not")
        exit()

    if argv[1] == "-u " or argv[1] == "-U":
        print("usage: ApplicationName AbsolutePath_of_Directory:")
        exit()

    try:
        Checkfile(argv[1])

    except Exception as E:
        print(str(E))

if __name__ == "__main__":
    main()