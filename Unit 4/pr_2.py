# write a program to handle multiple exceptions like SyntaxError and TypeError.

try:
    a = eval(input("enter first value : "))
    b = eval(input("enter second value : "))
    ans = a / b
except (TypeError,SyntaxError):
    print("Error")
else:
    print(ans)


'''
    v --> int
    v2 --> string
'''
