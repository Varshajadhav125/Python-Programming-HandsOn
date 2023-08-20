import os
from sys import *

def Checkfile(first,second):
    f = open(first,"r")
    f1 = open(second, "r")
    for elem in f:
        for elem1 in f1:
            if elem == elem1:
                print("Success")
            else:
                print("Failure")

def main():
    print("Application started")
    print("Application Name",argv[0])

    if len(argv) < 3:
        print("Insufficient Argument:")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This script is used to check file is exist or not")
        exit()

    if argv[1] == "-u " or argv[1] == "-U":
        print("usage: ApplicationName AbsolutePath_of_Directory:")
        exit()

    try:
        Checkfile(argv[1],argv[2])

    except Exception as E:
        print(str(E))

if __name__ == "__main__":
    main()