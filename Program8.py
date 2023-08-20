print("Demonstrate of industrial programming:")

def Fun(no):
    i = 1
    while (i <= no):
        print("*")
        i = i + 1

def main():
    print("Enter the number :")
    num = int(input())
    Fun(num)




if __name__ == "__main__":
    main()