# write a python program to handle some built in exceptions like ZeroDivisionError

a = int(input("Enter a divident : "))
b = int(input("Enter a divisor : "))

try:
    Ans = a / b
except ZeroDivisionError:
    print("ZeroDivisionError occure")
else:
    print("Answer : ", Ans)