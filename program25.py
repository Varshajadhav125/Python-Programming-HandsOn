
def main():
    list = []
    print("Enetr how many element you want to store:")
    size = int(input())
    for i in range(0,size):
        no = int(input())
        list.append(no)
    print(list)
    print("Enter no which you want to find in list")
    search = int(input())
    count = 0
    for no in list:
        if no == search:
            count = count + 1
    print("frequency is",count)


if __name__ == "__main__":
    main()