def fact(no):
    i= 1
    fact = 1
    while(i <= no):
        fact = fact * i
        i = i + 1
    return fact



def main():
    print("Enter the number:")
    num = int(input())
    factorial = fact(num)
    print("factorial is",factorial)




if __name__ == "__main__":
    main()
