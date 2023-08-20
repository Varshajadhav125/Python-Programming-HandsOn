import time
import threading


def Evenfactor(integer):
    #print("Enter element you want to display")
    #no = int(input())
    add = 0
    for i in range(1,integer,1):
     if i % 2 == 0:
        add = add + i
    print("Even Number Addition",add)

def Oddfactor(integer):
    #print("Enter element you want to display")
    #no = int(input())
    add = 0
    for i in range(1,integer,1):
     if i % 2 != 0:
         add = add + i
    print("odd Number Addition",add)
def main():
    #no = int(input())
    #Even(2000)
    #Odd(2000)
    integer = 200000

    p1 = threading.Thread(target = Evenfactor,args = (integer,))
    p2 = threading.Thread(target= Oddfactor, args=(integer,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)