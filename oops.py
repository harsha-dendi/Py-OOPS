class calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b

    def getdata(self):
        print("It is a method in a class")

    def summation(self):
        return self.firstnumber + self.secondnumber + calculator.num


obj = calculator(2,3)
obj.getdata()
print(obj.summation())


obj1 = calculator(4, 5)
obj1.getdata()
print(obj1.summation())