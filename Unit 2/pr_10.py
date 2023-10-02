# write a program to show veriable length of arguments and its use.

def show_arguments(*args):
    print("The total arguments are : ", len(args))
    for i in range(len(args)):
        print(args[i])
        

show_arguments(1,2,3,4,5,6,7,8,"jay","deep","jeel")