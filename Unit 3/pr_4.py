# write a program to store data into instane using mutator methods. and retrieve data using accessor method.
# Accessor = getter
# Mutator = setter

class Student:
    # constructor
    def __init__(self):
        self.name = None
        self.age = None
        self.location = None
    
    # Mutator method
    def setData(self):
        name = input("Enter student name : ")
        self.name = name
        age = input("Enter student age : ")
        self.age = age
        loc = input("Enter student location : ")
        self.location = loc

    # Accessor method
    def getData(self):
        print("-------- STUDENT DETAILS -------")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Location : ", self.location)

s = Student()
s.setData()
s.getData()