# write a program to implement single inheritance in which two sub classes are derived from a sinple base class.

class Teacher:
    def __init__(self):
        print("Teacher constructor called")

class Std1(Teacher):
    def __init__(self):
        super().__init__()
        print("Student 1 constructor called")

class Std2(Teacher):
    def __init__(self):
        super().__init__()
        print("Student 2 constructor called")

print("------------------------")
s1 = Std1()

print("------------------------")
s2 = Std2()
