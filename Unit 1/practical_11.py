# write a program to search an element in the list using for in loop and also demonstrates the use of else with for loop

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
search_ele = 10

for i in myList:
    if i == search_ele:
        print("Element found")
    else:
        continue