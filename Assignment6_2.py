class Circle:
    PI = 3.14
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        Radius = int(input("Enter radius: "))
        self.radius = Radius

    def CalculateArea(self):
        self.area = self.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * self.PI * self.radius

    def Display(self):
        print("Radius: ", self.radius)
        print("Area: ", self.area)
        print("Cicumference: ", self.circumference)

def main():
    Obj1 = Circle()
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2 = Circle()
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

if __name__=="__main__":
    main()
