import os
from sys import *


def Checkfile(file_Name):

    if os.path.exists(file_Name):
        print("file is exists")

    else:
        print("File is not exists")

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

    except:
        print("invalid input")


if __name__ == "__main__":
    main()