# create a program to retrieve, display and update only a range of elements from an array using indexing and slicing on an array.

import array 

# creating an array
a = array.array("i",[1,2,3,4,5])

# display array
print(a, type(a))

# updating an array
a[0] = 10000
print(a, type(a))

# updating array using slicing
a[0:3] = array.array("i",[101,202,303])
print(a, type(a))
