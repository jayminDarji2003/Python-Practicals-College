# write a program to implement multiple inheritance using two base classes

class College:
    name = "kirc"
    gmail = "kirc@gmail.com"
    address = "kalol"

    def __init__(self):
        print("College constructor called")

    @classmethod
    def getClgData(cls):
        print("----------------------------------------")
        print("Name of college : ", cls.name)
        print("College address : ", cls.address)
        print("College email : ", cls.gmail)


class Professor:
    name = "Alpesh Gajjar"
    age = 44
    subject = "Python"

    def __init__(self):
        print("Professor constructor called")

    @classmethod
    def getProfData(cls):
        print("------------------------------------------")
        print("Professor name : ", cls.name)
        print("Professor age : ", cls.age)
        print("Professor take subject : ", cls.subject)

class Student(College,Professor):
    def display(self):
        College.getClgData()
        Professor.getProfData()

s = Student()
s.display()
    