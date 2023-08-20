def display(No):
    if(No < 10):
        return No
    else:
        return (No % 10 * display(int(No / 10)))

def main():
    num = int(input("Enter the number"))
    ret = display(num)
    print("Factorial is",ret)


if __name__ == "__main__":
    main()