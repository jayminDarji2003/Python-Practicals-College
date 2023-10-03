# write a program to access the base class constructor from the sub class by using super() method and also without using super() method.

class Parent:
    # constructor
    def __init__(self,name=None,age=None):
        self.name = name
        self.age = age
    
    # display data
    def getData(self):
        print("--------------------------------")
        print("Name : ", self.name)
        print("Age : ", self.age)

class Child(Parent):
    # using super class constructor
    # def __init__(self,name=None,age=None):
    #     super().__init__(name,age)
    #     super().getData()

    # without super class constructor
    def __init_(self,name=None,age=None):
        pass


ch1 = Child("deep",19) # using super() method
ch1.getData()

