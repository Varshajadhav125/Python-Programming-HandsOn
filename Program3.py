print("Demonstration of industrial programming")

def Add(no1,no2):
    Ans = no1 + no2
    return Ans


def main():
    print("Enter first number")
    num1 = int(input())
    print("Enter second number")
    num2 = int(input())
    sum = Add(num1,num2)
    print("Addition is",sum)


if __name__ == '__main__':
    main()