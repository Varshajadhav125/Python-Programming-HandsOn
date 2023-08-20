import time
import threading


def Evenlist(list):
    #print("Enter element you want to display")
    #no = int(input())
    add = 0
    for i in range(1,len(list)):
     if list[i] % 2 == 0:
        add = add + list[i]
    print("Even Number Addition",add)

def Oddlist(list):
    #print("Enter element you want to display")
    #no = int(input())
    add = 0
    for i in range(0,len(list)):
     if list[i] % 2 != 0:
         add = add + list[i]
    print("odd Number Addition",add)
def main():
    #no = int(input())
    #Even(2000)
    #Odd(2000)
    #list = [1,2,3,4,5,6,7,8,9,10]
    list = []
    print("Enter the list size")
    size = int(input())
    for i in range(1,size + 1,1):
        no = int(input())
        list.append(no)
    print(list)
    p1 = threading.Thread(target = Evenlist,args = (list,))
    p2 = threading.Thread(target= Oddlist, args=(list,))

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