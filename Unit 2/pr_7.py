# write a python program that removes any repeated items from a list so that item can appear at list one time.

# Brute force approach : for beginners.
myList = [1,1,2,3,4,4,5,6,7,8,8,8,9,10]
new_list = []

for i in myList:
    if i not in new_list:
        new_list.append(i)

print(new_list)


# another approach : remove just in the original list
# advance approach
my_list = [1,1,2,3,4,4,5,6,7,8,8,8,9,10]

for i in my_list:
    if (my_list.count(i) > 1):
        my_list.remove(i)

print(my_list)