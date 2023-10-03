# student class
class Student:
    def __init__(self,id=None,name=None,marks=None):
        self.id = id
        self.name = name
        self.marks = marks

    # print data
    def display(self):
        print("--------------------------------")
        print("Id = ", self.id)
        print("Name = ", self.name)
        print("Marks = ", self.marks)

    # set data methods
    def setId(self,id):
        self.id = id
    
    def setName(self,name):
        self.name = name
    
    def setMarks(self,marks):
        self.marks = marks

    # get data methods
    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getMarks(self):
        return self.marks
    
    

