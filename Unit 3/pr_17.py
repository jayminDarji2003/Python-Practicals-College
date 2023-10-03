# Write a program to show method overloading to find the sum of two and three numbers.

class Operation:
    def __init__(self):
        print("constructor called")

    @classmethod
    def sum(self, x=None, y=None, z=None):
        if (y,z) is None and x is not None:
            return x
        elif (z is None) and (x,y) is not None:
            return x+y
        elif (x,y,z) is not None:
            return x+y+z
        else:
            print("You should pass a value to sum.")

print(Operation.sum(10,20))
print(Operation.sum(10,20,30))
