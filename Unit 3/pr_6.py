# write a program to create a static method that counts the number of instance created for that class

class myClass:
    n = 0
    def __init__(self):
        myClass.n += 1
    
    #staic method
    @staticmethod
    def count():
        print("No of instances created for this class = ", myClass.n)


a = myClass()
b = myClass()
c = myClass()
myClass.count()