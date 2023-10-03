# create a Student class to with the methods set_id,get_id, set_name, get_name, set_marks, get_marks. -> save with Student.py
# create a another file and import student class 

from Student import Student

std1 = Student()
std1.display()

# set details
std1.setId(101)
std1.setName("jaydeep")
std1.setMarks(99)

# get details
print("id : ", std1.getId())
print("name : ", std1.getName())
print("marks : ", std1.getMarks())

std1.display()
