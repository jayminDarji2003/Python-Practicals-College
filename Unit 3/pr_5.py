# write a program to use class method to handle the common features of all the instances of student class.

class Student:
    marks = 10
    @classmethod
    def modify(cls,name):
        print("{} scored {} marks".format(name, cls.marks))

Student.modify("sanjay")
Student.modify("sanjeev")