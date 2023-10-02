# write a program to find out and display the common and non-common elements in the list using the membership operators.

# membership operators : in , not in

my_list = [1,2,3,4,5]
a = 10
b = 2

if a in my_list:
    print("A is Member")
elif b in my_list:
    print("B is Member")
else:
    print("Both are not in the member.")


print("-------------------------")
# actual program for this program should be as follows,
# You can use membership operators like in to find common and non-common elements in two lists. Here's a Python program to do that:

# defining two lists
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

# create two list to store common and non-common elements
common_ele = []
non_common_ele = []

# find and store common elements using in operatos
for item in list1:
    if item in list2:
        common_ele.append(item)

# find and store non-common elements of list1
for item in list1:
    if item not in list2:
        non_common_ele.append(item)

# find and store non-common elements of list2
for item in list2:
    if item not in list1:
        non_common_ele.append(item)

# printing the common and non-common elements
print("common elements : " , common_ele)
print("non-common elements : " , non_common_ele)






