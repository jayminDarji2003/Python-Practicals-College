# write a python program to find sum of even numbers using command line arguments.

# import module
# import sys
# sum = 0

# print(sys.argv)
# print(type(sys.argv))

# for i in sys.argv:
#     if i is sys.argv[0]:
#         continue
#     if i % 2 == 0:
#         sum+=i

# print("The sum of evan numbers : " , sum)


print("----------------------------------------------------------------")
# actual program should be

import sys

# Initialize a variable to store the sum of even numbers
even_sum = 0

# Check if there are command line arguments
if len(sys.argv) < 2:
    print("Usage: python sum_even_numbers.py number1 number2 ...")
    sys.exit(1)

# Iterate through command line arguments starting from the second argument (index 1)
for arg in sys.argv[1:]:
    try:
        number = int(arg)  # Convert the argument to an integer
        if number % 2 == 0:  # Check if the number is even
            even_sum += number  # Add the even number to the sum
    except ValueError:
        print(f"Ignoring non-integer argument: {arg}")

# Print the sum of even numbers
print("Sum of even numbers:", even_sum)
