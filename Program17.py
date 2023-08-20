def Pattern(no):
    for i in range(0,no):
        for j in range(1,no+1):
                print(j,end = " ")
        print("\r")




def main():
    print("Enter the number")
    num = int(input())
    Pattern(num)





if __name__ == "__main__":
    main()