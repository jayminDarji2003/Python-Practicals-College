# Take a CM from user and convert to inches.

cm = int(input("Enter centimeter value : "))
# cm = 10
if cm < 0:
    print("Please enter positive value")
else:
    inches = cm / 2.54
    print("The inches value is : ", inches)