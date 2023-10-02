# write a program to evaluate the expression using eval() function.Input should be given by uers.

# taking expression from user
exp = input("Enter the expression : ")
ans = eval(exp)
print("The ans for this expression is : %.3f" %ans)