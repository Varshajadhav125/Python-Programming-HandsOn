def primenum(n):
    flag = True
    for i in range(2,int(n/2)+1,1):
        if n % i == 0:
            flag = False
            break
    return flag
def main():
    list = []
    sum = 0
    print("Enter the element you want to store:")
    size= int(input())
    print("Enter element in list")
    for i in range(0,size):
        no = int(input())
        list.append(no)
    print(list)
    for no in list:
        flag = primenum(no)
        if flag is True:
            sum = sum + no
    print(sum)

if __name__=="__main__":
    main()
    