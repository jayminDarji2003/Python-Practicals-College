# write a program to overload the addition operator (+) to make it act on the class objects.

class A:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages + other.pages

class B:
    def __init__(self,pages):
        self.pages = pages

x = A(100)
y = B(200)
print("Total pages : ", (x+y))

