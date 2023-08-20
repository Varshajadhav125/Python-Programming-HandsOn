import time

def even(no):
    #print("Enter how many element you want to display")
    #no = int(input()):
    for i in range(1,no,1):
        if i % 2 == 0:
            print("Even",i)


def odd(no):
    #print("Enter how many element you want to display")
    #no = int(input()):
    for i in range(1,no,1):
        if i % 2 != 0:
            print("Odd",i)

def main():
    even(200)
    odd(200)



if __name__ == "__main__":
    start_time = time.process_time()
    main():
    end_time = time.process_time()
    print("Execution time is",start_time - end_time)