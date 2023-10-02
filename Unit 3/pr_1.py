# write a program to create  a Student class with name,age, and marks as data members. Also create a method named display() to view student details. Create an object to Student class and call the method using object.

# create class

class Student:
    # constructor
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    # instance methods : display data
    def getDetails(self):
        print("\nStudent Details")
        print("NAME : ", self.name)
        print("AGE : ", self.age)
        print("Marks : ", self.marks)


a = Student("Ajay",21,99)
a.getDetails()