# Write a program to create an array from another array.

# importing module to create an array.
import numpy

# creating list
myList = [1,2,3,4,5,6,7,8,9,10]
# creating an array.
myArray = numpy.array(myList)
print(myArray, type(myArray))

# creating new array.
newArray = myArray
print(newArray, type(newArray))

# printing an address of the array.
print("The address of old array is ", id(myArray))
print("The address of new array is ", id(newArray))

if (id(myArray) is id(newArray)):
    print("Both arrays are same")
else: 
    print("Both arrays are different")


# how this questions answer given in the book.
print("--------------------------------")

x = [1,2,3,4,5,6,7,8,9,10]
print("Original array: ", x)

y = []
y[:] = x

print("New array: ", y)

print("The address of old array is ", id(x))
print("The address of new array is ", id(y))

if (id(x) is id(y)):
    print("Both arrays are same")
else: 
    print("Both arrays are different")