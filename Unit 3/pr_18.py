# write a program to override the super class method in subclass.

import math

class square:
    def area(self,x):
        print("Area of square is : ", x*x)
    
class circle(square):
    def area(self,x):
        print("Area of circle is : %.2f" %(math.pi * x * x))

c = circle()
c.area(10)
