comparision = lambda no:(no >= 70) and (no <= 90)

increment = lambda no:no + 10

product = lambda no1,no2:no1 * no2


def filterx(Arr,function_name):
    result = []
    for no in Arr:
        if(function_name(no)):
            result.append(no)
    return result

def Mapx(Arr,function_name):
    result = []
    for no in Arr:
        value = function_name(no)
        result.append(value)
    return result

def reduceX(Arr,function_Name):
    Ans = 1
    for no in Arr:
        Ans = function_Name(Ans,no)
    return Ans


def main():
    Data = []
    print("Enter the size of list")
    size = int(input())

    print("Enter element in list")
    for i in range(0,size):
        no = int(input())
        Data.append(no)
    print("original list",Data)
    fiter_Data = list(filterx(Data,comparision))
    print("Filter data",fiter_Data)

    Map_Data = list(Mapx(fiter_Data,increment))
    print("Mapped data",Map_Data)

    reduce_Data = reduceX(Map_Data,product)
    print("Reduced data",reduce_Data)


if __name__ == "__main__":
    main()