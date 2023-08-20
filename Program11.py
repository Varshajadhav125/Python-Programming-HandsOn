import Arithmetic as Arth

def main():
    print("Enter the first Number:")
    no = int(input())
    print("Enter the second Number:")
    no1 = int(input())

    Addition = Arth.Add(no,no1)
    print("Addition is",Addition)

    Sub = Arth.sub(no,no1)
    print("Substraction is",Sub)

    Multi = Arth.mul(no,no1)
    print("Multipication is",Multi)

    division = Arth.div(no,no1)
    print("division is",division)






if __name__ == "__main__":
    main()


