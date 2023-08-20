def fact(no):

   fact = 0
   for i in range(1,no):
       if(no % i == 0):
           fact = fact + i

   return fact



def main():
    print("Enter the number:")
    num = int(input())

    factorial = fact(num)
    print("Factorial is",factorial)





if __name__ == "__main__":
    main()