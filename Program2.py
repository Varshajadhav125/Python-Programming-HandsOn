print("Demonstration of industrial programming")

def checkSum(no):
    if(no % 2 == 0):
        print("EvenNumber")
    else:
         print("oddNumber")
    return no



def main():
    print("Enter any number")
    num = int(input())

    Ans = checkSum(num)
    print("Number is",Ans)

if __name__ == "__main__":
    main()
