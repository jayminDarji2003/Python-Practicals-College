# function
def my_function():
    print("Hello from my_function")

my_function()

# lambda function
# this function declare without name
# ex 1
cube = lambda x : x*x*x
print(cube(5))

# ex 2
cube2 = lambda : print("hello from lambda function")
print(cube2())



# Map, Filter, and Reduce 

# Map

def cube(x):
    return x*x*x
# print(cube(5))

# one way to do this things but we use map function
l = [1,2,3,4,5,6,7,8]
# finalList = [] 
# for item in l:
#     finalList.append(cube(item))
# print(finalList)

finalList = list(map(lambda x : x*x*x,l))
print(finalList)

# Filter function
# takes (arguments) --> function and list
my_list = [1,2,3,4,5,6,7,8,9]
final_list = list(filter(lambda x : x%2==0 , my_list))
print(final_list)


# Reduce
from functools import reduce  # importing reduce

my_list2 = [10,20,30,40,50,60,70,80,90]
final_list2 = reduce(lambda x,y: x+y,my_list2)
print(final_list2)






import os
os.system("cls")  # is used to clear terminal
print("hello world")

# list 

#create a list
myList = ["ram","shyam",10,True]
print(myList)

# Accessing item from a list
print(myList[1],type(myList[1]))

# Negative indexing
print(myList[-1])
# It is automatically write --> len(myList) - 1

# slice of a list
print(myList[1:4]) # start from 1 and go till 4, 4 is not inclusive

# create a list using range() function
# rangeList = [range(10,20,1)]
# print(rangeList)

# update the elements of the list
li = [1,2,3,4,5]
li[2] = 1000
print(li)

print("-------------------------------------------------------")

# concatenate the list

# using + operator
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)

# using append() method with for loop
l1 = [1,2,3]
l2 = [4,5,6]
for i in l2:
    l1.append(i)
print(l1)

# cloning the list

# using slicing technique
def CloningList(myList):
    copy_list = myList[:]
    return copy_list

thisList = [1,2,3,4,5]
copyList = CloningList(thisList)
print("Original list : " , thisList)
print("Cloning list : " , copyList)

print("------------------------------------------------------------")

# using extend() method
def CloningList(myList):
    copy_list = []
    copy_list.extend(myList)
    return copy_list

thisList = [1,2,3,4,5]
copyList = CloningList(thisList)
print("Original list : " , thisList)
print("Cloning list : " , copyList)

print("------------------------------------------------------------")

# using list() method
def CloningList2(myList):
    copy_list = list(myList)
    return copy_list

thisList2 = [1,2,3,4,5]
copyList2 = CloningList(thisList2)
print("Original list : " , thisList2)
print("Cloning list : " , copyList2)

print("------------------ List methods ----------------------")

# append() method
a = [1,2,3,4,5]
a.append(100)
print(a)

# insert() method
a2 = [1,2,3,4,5]
a2.insert(3,100)
print(a2)

# extend() method
li1 = [1,2,3,4,5]
li2 = [10,11,12,13]
li1.extend(li2)
print(li1)

# sum() method
thiList = [1,2,3,4,5]
print(sum(thiList))

# count() method
listt = [1,2,3,4,5,1,2,5,7,1,5,1]
print(listt.count(1))

# len() method
thissList = [1,2,3,4,5,6]
print(len(thissList))

print("----------------------------------------------------------------")


# Tuples in python 
'''
    Tuple is similar to a list in some cases.
    Tuple is a collection of any types of elements
    Tuple is immutable, so we can not modify or change it.
    Tuple can not contains duplicates.
'''

# create a tuple
# way 1
t1 = 'java', 'python', 'c#'
print(t1)
print(type(t1))
# way 2
t2 = ('java', 'python', 'c#')
print(t2)
print(type(t1))

# concate two tuples
tuple3 = t1 + t2
print(tuple3)

# Rule 1 : Immutable
t3 = (1,2,3,4,5)
# t3[1] = 1000 # throws an error
print(t3)

# Nesting of tuples
t5 = (5,6,6,7)
t6 = (90,89,78)
nestTuple = ("java", "python", "c#" , t5, t6)
print(nestTuple)

# Repetition in tuples
t7 = ("jaymin", ) * 5
print(t7)
print(type(t7))

# Slicing of tuples
myTuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
print(myTuple[3:9])
print(myTuple[3:])
print(myTuple[:9])
print(myTuple[:])
print(myTuple[:-10])
print(myTuple[-10:])
print(myTuple[::-1])

# Deleting tuples
thisTupe = (1,2,3,4,5,6,7,8)
del thisTupe
# print(thisTupe) # throws an error because this tuple is not exists

# Converting List to Tuples
list1 = [1,2,3,4,5,6,7,8]
myTuple2 = tuple(list1)
print(list1) 
print(myTuple2) 
print(type(myTuple2)) 

# converting tuples to list
tuple4 = (1,2,3,4,5,6,8)
convertList = list(tuple4)
print(tuple4)  
print(convertList) 


# Dictionary

dict = {
    1 : 'jaymin',
    2 : 'kishan'
}
print(dict.items())


