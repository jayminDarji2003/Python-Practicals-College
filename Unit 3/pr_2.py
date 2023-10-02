# write a program to create Student class with a constuctor having more than one parameter

class Student:
    # constructor
    def __init__(self,name,age,description):
        self.name = name
        self.age = age
        self.description = description
    
    # instance method : display student details
    def getData(self):
        print("Student name : " ,self.name)
        print("Student age : ", self.age)
        print("Student description : " , self.description)

s = Student("Dhruv",21,"Dhruv is a very inteligent student")
s.getData()