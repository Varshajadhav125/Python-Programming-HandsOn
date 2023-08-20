class BankAccount:

    ROI = 10.5
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def Deposit(self,value):
        self.amount = self.amount + value
        print("after Deposit",self.amount)


    def withdraw(self,value):
        self.amount = self.amount - value
        print("after withdraw",self.amount)


    def calculateinterest(self):
        Ans = 10000*(0.1*5)
        totalamount = Ans - 10000
        print("total interest is",totalamount)

    def Display(self):
        print("Name of Accountholder",self.name)
        print("Amount is",self.amount)


def main():
    obj = BankAccount("varsha",20000)
    obj1 = BankAccount("Divya",30000)

    obj.Deposit(500)
    obj.withdraw(100)
    obj.calculateinterest()
    obj.Display()

    print()
    obj1.Deposit(400)
    obj1.withdraw(200)
    obj1.calculateinterest()
    obj1.Display()


if __name__ == "__main__":
    main()