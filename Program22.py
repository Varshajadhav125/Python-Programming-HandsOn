def main():
    list = []
    print("Enter how many element you want to store:")
    size = int(input())
    sum = 0

    print("please enter the element:")
    for i in range(0,size):
        no = int(input())
        list.append(no)
        sum = sum + no
    print(list)
    print("Addition is",sum)


if __name__ == "__main__":
    main()