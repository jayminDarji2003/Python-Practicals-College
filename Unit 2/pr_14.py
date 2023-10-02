# write a program to create a list using range functions perform append,update and delete element operations on it.

# creating a empty list
myList = []

# adding elements to the list using range function
for i in range(0,11):
    myList.append(i)

# printing the list
print(myList)

# updating the list
myList.insert(7,800)
print(myList)

# deleting elements from the list
myList.remove(7)
print(myList)