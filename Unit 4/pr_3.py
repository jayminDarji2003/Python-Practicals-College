# write a program to import "os" module and print the current working directory and returns a list of all modules functions.

import os

# return the absolute path 
print(os.getcwd())

# return the list of function of os
listOfunctions = list(dir(os))

for i in listOfunctions:
    print(i)