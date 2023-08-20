import os
from sys import *

def Checkfile(first,str):
    f = open(first,"r")
    text = f.read()
    Data = text.count(str)
    print("Frequency is",Data)

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