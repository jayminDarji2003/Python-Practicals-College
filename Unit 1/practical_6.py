# Create program to display memory location of two variables using id() function, and then use identity operators two compare wheather two objects are same or not.

# identity operators : is , not is

a = 20
b = 20

if (a is b):
    print("Both are in same Location")
else:
    print("Both are not in same Location")

if (id(a) == id(b)):
    print("Both are in the same Location")
else:
    print("Both are not in the same Location")

b = 40
if (a is b):
    print("Both are in the same Location")
else:
    print("Both are not in the same Location")

if (a is not b):
    print("Both are not in the same Location")
else:
    print("Both are not in the same Location")


print("-------------------------")

# actual program for this program should be as follows,

# define two variables
var1 = "Hello"
var2 = "Hello"

# getting the memory location of the variables using id() function
id_var1 = id(var1)
id_var2 = id(var2)

# identify operator to compare two variables
if id_var1 is id_var2:
    print("Both are same")
else:
    print("Both are not same")


# display memory locations
print("The memory location of the var1 : ", id_var1)
print("The memory location of the var2 : : ", id_var2)

