class Arithmetic:
    def __init__(self):
        self.value = 0
        self.value1 = 0

    def Accept(self):
        print("Enter first number")
        self.value = int(input())

        print("Enter second number")
        self.value1 = int(input())


    def Addition(self):
        result = self.value + self.value1
        return result

    def Substraction(self):
        result = self.value - self.value1
        return result

    def Multiplication(self):
        result = self.value * self.value1
        return result

    def Division(self):
        result = self.value / self.value1
        return result



def main():
    obj = Arithmetic()
    obj1 = Arithmetic()
    obj2 = Arithmetic()

    obj.Accept()
    output = obj.Addition()
    print("Addition is",output)

    output = obj.Substraction()
    print("Substraction is",output)

    output = obj.Multiplication()
    print("Multiplication is",output)

    output = obj.Division()
    print("Divvision is",output)

    print("\n")

    obj1.Accept()
    output = obj1.Addition()
    print("Addition is", output)

    output = obj1.Substraction()
    print("Substraction is", output)

    output = obj1.Multiplication()
    print("Multiplication is", output)

    output = obj1.Division()
    print("Divvision is", output)

    print("\n")

    obj2.Accept()
    output = obj2.Addition()
    print("Addition is", output)

    output = obj2.Substraction()
    print("Substraction is", output)

    output = obj2.Multiplication()
    print("Multiplication is", output)

    output = obj2.Division()
    print("Divvision is", output)


if __name__ == "__main__":
    main()