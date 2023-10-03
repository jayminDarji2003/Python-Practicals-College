# Write a program to override super class constructor and method in sub class.

class Teacher:
    # constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Super class constructor called")
    
    # display data
    def display(self):
        print("------------------------------------")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Data fetch from super class")

class Student(Teacher):
    # constructor
    def __init__(self,name,age):
        # super().__init__(name,age)
        self.name = name
        self.age = age
    
    # display data
    def display(self):
        # super().display()
        print("------------------------------------")
        print("Name : ", self.name)
        print("Age : ", self.age)

st = Student("Kishan",90)
st.display()
