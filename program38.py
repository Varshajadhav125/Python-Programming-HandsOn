import time
import threading


def Even(no):
    #print("Enter element you want to display")
    #no = int(input())
    for i in range(1,no,1):
     if i % 2 == 0:
        print("Even Number",i)

def Odd(no):
    #print("Enter element you want to display")
    #no = int(input())
    for i in range(1,no,1):
     if i % 2 != 0:
        print("odd Number",i)
def main():
    #no = int(input())
    #Even(2000)
    #Odd(2000)
    number = 2000

    p1 = threading.Thread(target = Even,args = (number,))
    p2 = threading.Thread(target= Odd, args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of execution")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)