import time
import threading

def small(string):
    count = 0
    print("small letters")
    for i in range(len(string)):
        if (string[i] >= 'a' and string[i] <= 'z'):
            count = count + 1
            print(string[i])
            print("Id ",i)
    print("small letter count is",count)


def capital(string):
    count = 0
    print("capital letter")
    for i in range(len(string)):
        if (string[i] >= 'A' and string[i] <= 'Z'):
            count = count + 1
            print(string[i])
            print("id",i)
    print("Capital letter count",count)

def digit(string):
    count = 0
    print("digits")
    for i in range(len(string)):
        if (string[i] >= '0' and string[i] <= '9'):
            count = count + 1
            print(string[i])
            print("Id",i)
    print("Digit count is",count)


def main():
    #string = "I Am Varsha Jadhav In 1290786543256789076543256789TH Class"
    print("Enter string")
    string = input()

    p1 = threading.Thread(target = small,args = (string,))
    p2 = threading.Thread(target = capital,args = (string,))
    p3 = threading.Thread(target = digit,args = (string,))

    p1.start()
    p1.join()
    print()

    p2.start()
    p2.join()
    print()

    p3.start()
    p3.join()
    print()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is",end_time - start_time)