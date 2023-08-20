#import Arithmetic1

import Arithmetic1 from *

def main():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))

    ret = Arithmetic1.Add(num1,num2)
    print("Addition is",ret)

    ret = Arithmetic1.Sub(num1, num2)
    print("Addition is", ret)

    ret = Arithmetic1.mul(num1, num2)
    print("Addition is", ret)

    ret = Arithmetic1.div(num1, num2)
    print("Addition is", ret)


if __name__ == "__main__":
    main()