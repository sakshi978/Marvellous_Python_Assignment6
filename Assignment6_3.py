class Arithmatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        Value1 = int(input("Enter 1st no.: "))
        self.value1 = Value1

        Value2 = int(input("Enter 2nd no.: "))
        self.value2 = Value2

    def Addition(self):
        return self.value1+self.value2

    def Subtraction(self):
        return self.value1-self.value2

    def Multiplication(self):
        return self.value1*self.value2

    def Division(self):
        return self.value1/self.value2

def main():
    Obj1 = Arithmatic()
    Obj1.Accept()

    iRet1 = Obj1.Addition()
    print("Addition: ", iRet1)

    iRet2 = Obj1.Subtraction()
    print("Subtraction: ", iRet2)

    iRet3 = Obj1.Multiplication()
    print("Multiplication: ", iRet3)

    iRet4 = Obj1.Division()
    print("Division: ", iRet4)

if __name__=="__main__":
    main()