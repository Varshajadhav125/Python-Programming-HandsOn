def display(no):
    if (no < 10):
        return no
    else:
        return (no % 10 + display(no/10))


def main():
    num = int(input("Enter the number:"))
    Add = display(num)
    print("Addition is",Add)


if __name__ == "__main__":
    main()
