# # None datatype 
# var = None
# if var is not None:
#     print("Not a variable")
# else:
#     print("Variable")

# # Numeric datatype 
# """
#     Three types of Numeric datatypes
#         1.Integer --> 10,20
#         2.Float   --> 10.23 , 90.00
#         3.Complex --> 10+3j
# """

# # Sequence in Python 
# '''
#     1. List -> [1,2,3]  -> List is mutable
#         ->List is a collection of values which is multable and ordered.
#     2. Tuple -> (1,2,3) -> Tuple is immutable
#         ->Tuple is a collection of values which is immutable and ordered also allow duplicates values
#     3. String -> JAYMIN -> String is immutable
# '''
# # EX 
# MyList1 = [10,20,30,40,50,60]
# MyList2 = [70,80,90,100,110]

# if 50 in MyList1:
#     print("contains")

# if 500 not in MyList1:
#     print("not contains")

# print(MyList1 + MyList2)
# print(MyList1 * 3)
# print(max(MyList1))
# print(min(MyList1))
# print(MyList1.count(10))
# print(MyList1[2:5])
# print(MyList2[1:5:2])

# MyList1.append(1000) # add to last
# print(MyList1)

# MyList2.insert(3,70000)
# print(MyList2)

# MyList2.pop()
# MyList2.pop(3)
# print(MyList2)

# MyList1.reverse()
# print(MyList1)

# MyList1.clear() 
# print(MyList1)

# # str() method 
# x = 70.70
# y = str(x)
# print(type(y) , y)

# bytes() method
# a = 100
# a1 = bytes(a)
# print(type(a1))


# range() method
# '''
#     range() method returns a set of values from a perticular range.start from 0 bydefault and increased by 1 and last value is exclusive

#     syntax : range(start,stop,step)
# '''
# print("-----------------------------------------------------")
# p = range(1,10)
# print(p)
# for n in p:
#     print(n)


# sets
# '''
#     sets is a collection of values which is unordered and unindexed.
#     set write in curly brackets.
# '''

# myset = {"a", "b", "c", "d", "e", "f"}
# print(myset)
#this is for in loop
# for x in myset:
#     print(x)

# if "c" in myset:
#     print("contains")

# myset.add("100")
# print(myset)

# myset.update(["1000","2000","3000","4000","5000"])
# print(myset)

# print(len(myset))

# myset.remove("1000")
# print(myset)

# myset.discard("100")
# print(myset)

# myset.clear()
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set22 = {1, 2, 3}
# set222 = {1, 2, 3}
# set3 = set1.union(set2,set22,set222)
# print(set3)

# del set3
# print(set3) #this code will give error because it is deleted

# Dictionaries
# it is same as object in javascript
# myDict = {
#     "ten":10,
#     "twenty" : 20,
#     "thirty" : 30,
#     "fourty" : 40,
#     "fifty" : 50,
# }

# print(myDict)
# print(myDict.keys())
# print(myDict.values())
# keyType = type(myDict.keys())
# print(keyType)

# print("--------------------------------")
# name = input("enter your name : ")
# print(name)



# // called floor division
# a = 3
# b = 10
# print(b//a)

# input in python and multiple inputs

# num = input("Enter a num : ") #single input in python
# number,number2 = input("Enter a number : ").split() #multiple inputs in python
# print(num)
# print(number,number2)

# Command line arguments
# import sys
# print(sys.argv)
# print(len(sys.argv))


# Conditional statements
# '''
#     1. if
#     2. if else
#     3. if..elif..else
#     4. nested if..else
# '''

# print("hello world")
# print("hello world 2")
# print("hello world 3")

# import os
# os.system("cls")  # this will clear the console
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# if num1 > num2:
#     print("num1 is maximum")
# elif num1 < num2:
#     print("num2 is maximum")
# else:
#     print("both are same")


# loops in python
    # Types of loops
    #     1. while loop
    #     2. for loop
    #     3. nested loop
    # NOTE: we don't have do-while loop in python.


# while loop
# x = 1
# n = 10
# while x < n:
#     print(x)
#     x += 1

# for loop
# for i in range(1,10):
#     print(i)

# nested loop
# adj = ["red", "big" ,"tasty"]
# fruits = ["apple", "orange","banana"]

# for item in adj:
#     for fruit in fruits:
#         print(item , fruit)