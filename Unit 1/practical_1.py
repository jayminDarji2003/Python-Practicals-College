# swap two numbers without taking temporary values
num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))

num1 = num1+num2  # 10+20 = 30
num2 = num1-num2  # 30-20 = 10
num1 = num1-num2  # 30-10 = 20

print("The value of num1 is : " , num1)
print("The value of num2 is : " , num2)
