import time
import threading

def Thread1(number):
    print("Display number upto 50")
    for i in range(1,number+1):
        print(i)


def Thread2(number):
    print("Reverse number upto 50")
    for i in range(0,number + 1):
        no = number - i
        print(no)


def main():
    #thread1(50)
    #thread2(50)

    Number = 50

    #p1 = threading.Thread(target=DisplayEven, args=(Number,))
    #p2 = threading.Thread(target=DisplayOdd, args=(Number,))

    p1 = threading.Thread(target=Thread1, args=(Number,))
    p2 = threading.Thread(target=Thread2, args=(Number,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is",end_time - start_time)