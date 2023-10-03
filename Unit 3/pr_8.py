# write a program to create a Emp class and make all the members of the Emp class available to another class(myClass).[by passing members of one class to another class]

class Emp:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("--------------------------------")
        print("id =", self.id)
        print("name =", self.name)
        print("salary =", self.salary)

class myClass:
    @staticmethod
    def myMethod(e):
        e.salary += 1000
        e.display()

e = Emp(101,"Raj kundra",12000.23)
e.display() 

myClass.myMethod(e)
