even =lambda no:no % 2 == 0

square = lambda no:no * no

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

def reduceX(Arr):
    sum = 0
    for no in Arr:
        sum = sum + no
    return sum


def main():
    Data = []
    print("Enter the size of list")
    size = int(input())

    print("Enter element in list")
    for i in range(0,size):
        no = int(input())
        Data.append(no)
    print("original list",Data)
    fiter_Data = list(filterx(Data,even))
    print("Filter data",fiter_Data)

    Map_Data = list(Mapx(fiter_Data,square))
    print("Mapped data",Map_Data)

    reduce_Data = reduceX(Map_Data)
    print("Reduced data",reduce_Data)


if __name__ == "__main__":
    main()