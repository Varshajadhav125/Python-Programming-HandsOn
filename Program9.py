print("Demonstrate of industrial programming:")

def Fun(no):
    for i in range(1,no):
        if(i % 2==0):
            print(i)



def main():
    print("Enter the num")
    num = int(input())
    Fun(num)


if __name__ == '__main__':
    main()

