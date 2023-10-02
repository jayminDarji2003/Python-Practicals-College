# create a class

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def info(self):
        print(f"{self.name} ====> {self.age}")

a = Person("jaymin", 20)
a.info()

b = Person("Deep", 19)
b.info()

c = Person("Kishan", 18)
c.info()

d = Person("Het", 19)
d.info()

# Types of Constructors in class
'''
    There are two types of constructor in the class
        1. default constructor ->It takes only one argument which  is self and don't take any other arguments

        2. parameterized constructor -> It takes self and other parameters which needed to be passed to the constructor.
'''

# Types of Variables in class
'''
    There are two types of variable in the class
        1. Instance variable -> Declared inside the constructor
        2. class or static variable -> Declared inside the class but our of all methods.
'''

class Player:
    name = "Virat"
    age = 29

    def info(self):
        print("The player name is : ", self.name)
        print("The player age is : ", self.age)

print("--------------------------------")

a = Player()
a.info()

v = Player()
v.name = "Dhoni"
v.age = 58
v.info()

c = Player()
c.info()


print("--------------------------------")

# Types of Methods in class
'''
    There are three types of method in class
        1. Instance method
            a. Accessor method -> getters
            b. Mutator method  -> setters
        2. class method
        3. static method
'''

    
# Class method
class myClass:
    name = "student"

    @classmethod
    def getName(self):
        return self.name
    
print(myClass.getName())


# static method
class myStaticMethod:
    name = "student"

    @staticmethod
    def getName():
        return "This is static method"
    
print(myStaticMethod.getName())