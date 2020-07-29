class Demo:
    Value = 0
    def __init__(self, no1, no2):
        self.value1 = no1
        self.value2 = no2

    def Fun(self):
        print(self.value1, self.value2)

    def Gun(self):
        print(self.value1, self.value2)

def main():
    Obj1 = Demo(11,5)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()

    Obj1.Gun()
    Obj2.Gun()

if __name__=="__main__":
    main()