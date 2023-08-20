class Circle:
    Pi = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the readius of circle")
        self.Radius = int(input())

    def calculateArea(self):
        self.Area = Circle.Pi * self.Radius * self.Radius

    def calculateCircumference(self):
        self.Circumference = 2 * Circle.Pi * self.Radius

    def Display(self):

        print("radius of circle ",self.Radius)
        print("Area of circle",self.Area)
        print("circumference of circle",self.Circumference)



def main():
    obj = Circle()
    obj1 = Circle()
    obj2 = Circle()

    obj.Accept()
    obj.calculateArea()
    obj.calculateCircumference()
    obj.Display()

    obj1.Accept()
    obj1.calculateArea()
    obj1.calculateCircumference()
    obj1.Display()

    obj2.Accept()
    obj2.calculateArea()
    obj2.calculateCircumference()
    obj2.Display()

if __name__ == "__main__":
    main()