# write a program to assert the user enters a number greater than zero.

num = int(input("Enter a number: "))
assert num >= 0 , "Only positive numbers are allowed"
print("Entered number ", num)