def prime(no):
    flag = True
    for i in range(2,no):
        if no % i == 0:
            flag = False
            break
    return flag

def multiply(no):
    return (no * 2)

def filterx(Arr,function_name):
    result = []
    for no in Arr:
        flag=function_name(no)
        if flag is True:
            result.append(no)
    return result

def Mapx(Arr,Function_Name):
    result = []
    for no in Arr:
        value = Function_Name(no)
        result.append(value)
    return result

def ReduceX(Arr):
    max = 0
    for no in Arr:
        no > max
        max = no
    return max


def main():
    Data = []
    print("Enter the size of list")
    size = int(input())

    print("Enter element in list")
    for i in range(0,size):
        no = int(input())
        Data.append(no)
    print("original list",Data)
    filter_Data = list(filterx(Data,prime))
    print("Filter data",filter_Data)

    Map_Data = list(Mapx(filter_Data,multiply))
    print("Mapped Data",Map_Data)

    Reduce_Data = ReduceX(Map_Data)
    print("Reduce data",Reduce_Data)

if __name__ == "__main__":
    main()