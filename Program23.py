def main():
    list = []
    print("Enter how many element you want to store:")
    size = int(input())
    max = 0

    print("please enter the element:")
    for i in range(0,size):
        no = int(input())
        list.append(no)
        if (no > max):
            max = no
    print(list)
    print("max no",max)

if __name__ == "__main__":
    main()