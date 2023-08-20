print("Demonstrate of industrial programming:")

def Fun(str):
    count = 0
    for i in str:
        count = count + 1
    print(count)



def main():
    print("Enter the string:")
    str = input()
    Fun(str)


if __name__=="__main__":
    main()
