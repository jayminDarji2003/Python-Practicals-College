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


print("----------------------------------------------------------------")

# Inheritance in python
'''
    Inheritance is the reusability of code.  It has base class and derived class.
'''

# class Parent:
#     # constructor
#     def __init__(self):
#         print("Parent constructor called")
#         self.parentName = "Parent"

#     # instance method
#     def getName(self):
#         print("Parent Name is : ", self.parentName)

# class Child(Parent):
#     # constructor
#     def __init__(self):
#         print("Child constructor called")
#         self.childName = "Child"

#     # instance method
#     def getName(self):
#         print("Child Name is : ", self.childName)


# p = Parent()
# p.getName()

# c = Child()
# c.getName()


# write a program that will access the base class constructor from derived class.

class Teacher:
    def __init__(self,scName):
        self.schoolName = scName

    def display(self):
        print("The school name is : ", self.schoolName)

    def setName(self,name):
        self.schoolName = name

class Student(Teacher):
    # nothing doing // pass
    def print(self):
        print("this class nothing doing")

st = Student("KIRC CAMPUS")
st.display()
st.setName("BHAGINI VIDHYALAYA")
st.display()


# Constructor overriding and method overriding
class ts:
    def __init__(self,tsName):
        self.schoolname = tsName

    def display(self):
        print("School name: " + self.schoolname)

class st(ts):
    def __init__(self,tsname,std):
        self.schoolname = tsname
        self.std = std

    def display(self):
        print("School name: " + self.schoolname)
        print("std: " , self.std)

s = st("kirc",8)
s.display()

# super() method
# the super() method is used to give reference to the base class to child class.
class myClass:
    # constructor
    def __init__(self,msg):
        self.message = msg

    # instance method
    def display(self):
        print("The message is : ", self.message)
        print("Parent class")

class myChild(myClass):
    # constructor
    def __init__(self,msg):
        super().__init__(msg)
    
    # instance method
    def display(self):
        super().display()

ms = myChild("Keep learning and keep progressing")
ms.display()


# Types of inheritance
'''
    Two types of inheritance
        1. single inheritance
            --> one parent, lots of child
        2. multiple inheritance
            -> lots of parent and only one child
'''

# single inheritance example
class a:
    def display(self):
        print("Parent class")
class b(a):
    def display(self):
        super().display()
        print("Child class 1")
class c(a):
    def display(self):
        super().display()
        print("Child class 2")

print("--------------------------------")
x = b()
x.display()
y = c()
y.display()


# Multiple inheritance
# In multiple inheritance there are only one child and more than one parents

class Par1:
    def sum(self,a,b):
        return a+b
class Par2:
    def mul(self,a,b):
        return a*b
class Par3:
    def div(self,a,b):
        return a/b

class Child(Par1,Par2,Par3):
    def sub(self,a,b):
        return a-b
    
print("--------------------------------")
c = Child()
print(c.sum(10,20))
print(c.mul(10,20))
print(c.div(10,20))
print(c.sub(10,20))


# Mehtod Resoultion order
# ex

class A(object):
    def method(self):
        print("A class method")
        # super().method()
class B(object):
    def method(self):
        print("B class method")
        # super().method()
class C(object):
    def method(self):
        print("C class method")
        # super().method()

class x(A,B):
    def method(self):
        print("X class method")
        super().method()
    
class y(B,C):
    def method(self):
        print("Y class method")
        super().method()

class p(A,B,C):
    def method(self):
        print("P class method")
        super().method()

newp = p()
print(p.mro())
newp.method()


print("----------------------------------------------------------------")

# simple python program to demonstrate operator overloading

# + operator overloading
print(1 + 2)
print("Hello " + "World!")
print([1,2,3] + [4,5,6])

# * operator overloading
print(4 * 5)
print("Hello " * 3)


print("----------------------------------------------------------------")

# method overloading

class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif b is not None and c is None:
            return a + b
        elif b is not None and c is not None:
            return a + b + c

# Create an instance of the Calculator class
calc = Calculator()

# Examples of method overloading
result1 = calc.add(5)
result2 = calc.add(5, 10)
result3 = calc.add(5, 10, 15)

print(result1)  # Output: 5
print(result2)  # Output: 15
print(result3)  # Output: 30
