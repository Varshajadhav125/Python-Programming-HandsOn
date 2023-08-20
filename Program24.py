def main():
    list = []
    print("Enter how many element you want to store:")
    size = int(input())


    print("please enter the element:")
    for i in range(0,size):
        no = int(input())
        list.append(no)
        min = list[0]
    print(list)
    for i in range(0,size):
        for j in range(i+1,size):
            if (list[i] > list[j]):
                #temp = list[i]
                #list[i] = list[j]
                #list[j] =
                min = no

    #print("sorted list",list)

    #if (no < min):
        #min = no

    #print(list)
    print("min number is",min)

if __name__ == "__main__":
    main()