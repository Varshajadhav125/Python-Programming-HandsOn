def pattern(no):
    for i in range(0,no):
        for j in range(0,no):
            print("*",end = " ")
        print("\r")

def main():
    print("Enter the number:")
    num = int(input())

    result=pattern(num)
    #print("result is",result)

if __name__ == "__main__":
    main()