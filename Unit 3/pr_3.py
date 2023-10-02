# write a program to demonstrate the use of : instance, class, static methods

class test:
    college = "KIRC"

    # constructor
    def __init__(self):
        self.name = "jaymin"
        self.study = "BCA"

    # instance method
    def getData(self):
        print("NAME : ", self.name)
        print("Study : ", self.study)

    # class method
    @classmethod
    def setCollege(cls):
        cls.college = "KICS"

    # static method
    @staticmethod
    def getMax(x,y):
        return max(x,y)

a = test()

# instance method call
a.getData()

# class method call
test.setCollege()
print("College name : ", test.college)

# static method
print("Max : ", test.getMax(100,23))