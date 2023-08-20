def countdigit(no):
    add = 0
    while(no > 0):
        rem = no % 10
        no = no // 10
        add = add + rem
    return add




def main():
    print("Enter the number:")
    num = int(input())

    add = countdigit(num)
    print(add)

if __name__ == "__main__":
    main()