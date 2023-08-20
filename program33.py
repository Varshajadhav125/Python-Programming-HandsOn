class Demo:
    value = 0
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def fun(self):
        print("Display the first number",self.no1)
        print("Display the second number",self.no2)

    def gun(self):
        print("Display the first number", self.no1)
        print("Display the second number", self.no2)



def main():

    obj1 = Demo(10,12)
    obj2 = Demo(11,13)

    obj1.fun()
    obj1.gun()

    obj2.fun()
    obj2.gun()






if __name__ == "__main__":
    main()