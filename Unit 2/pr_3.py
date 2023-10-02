# Write a program to understand various methods of array class mentioned : append, remove, pop, index,tolist,count

list1 = [1,2,3,4,5,6,7,8,9,10]

# append
list1.append(10020)
print(list1)

# remove
list1.remove(10020)
print(list1)

# pop
list1.pop()
print(list1)

# index
i = list1.index(4)
print(i)

# count
print(list1.count(5))

# array method
import numpy as np
array = np.array(list1)
new_list = array.tolist()
print(new_list)
print(type(new_list))