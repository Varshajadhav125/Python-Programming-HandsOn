def display(no):
    if (no < 10):
        return no
    else:
        return (no % 10 + display(int(no / 10)))

def main():
    num = int(input("Enter the number:"))
    ret = display(num)
    print("Addition is ",ret)

if __name__ == "__main__":
    main()