class numbers:
    def __init__(self,value):
        self.val = value

    def checkPrime(self):
        
        for i in range(2,int(self.val)):
            if self.val % i == 0:
                print("Not prime",self.val)
                return False
        print("primeNumber",self.val)
        return True

    def checkperfect(self):
        sum = 0
        for i in range(1,int(self.val)):
            if self.val % i == 0:
                sum = sum + i
        if self.val == sum:
            print("Number is perfect",sum)
            return True
        else:
            print("Number is not perfect",sum)
            return False

    def factors(self):
        for i in range(1,self.val):
            if self.val % i == 0:
                 print("Factors are",i)

    def sumfactors(self):
        sum = 0
        for i in range(1, self.val):
            if self.val % i == 0:
                sum = sum + i
        print("Addition is", sum)


def main():
    print("Checking prime number")
    obj = numbers(13)
    print(obj.checkPrime())

    print()

    print("checking Perfect number")
    obj = numbers(6)
    print(obj.checkperfect())

    print()

    print("display factors")
    obj = numbers(8)
    print(obj.factors())

    print()

    print("Addition of factors")
    obj = numbers(9)
    print(obj.sumfactors())

    print()
    print("-------------------------------------------------------------------------------------------------------------------------")

    print("Checking prime number")
    obj1 = numbers(14)
    print(obj1.checkPrime())

    print()

    print("checking Perfect number")
    obj1 = numbers(7)
    print(obj1.checkperfect())

    print()

    print("display factors")
    obj1 = numbers(10)
    print(obj1.factors())

    print()

    print("Addition of factors")
    obj1 = numbers(11)
    print(obj1.sumfactors())


if __name__ == "__main__":
    main()