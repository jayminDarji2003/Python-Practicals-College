# write a program to demonstrate the use of positional arguments keyword and default arguments.print

# positional arguments
def positional_arguments(ram,shyam,harish):
    print("Positiona arguments : " ,ram,shyam,harish) 

# keyword arguments
def keyword_arguments(ram,shyam,harish):
    print("Keyword arguments : " ,ram,shyam,harish)

# default arguments 
def default_arguments(ram,shyam = "Shyam",harish = "Harish"):
    print("Default arguments : " ,ram,shyam,harish)

a = "Ram"
b = "Shyam"
c = "Harish"

# positional arguments
positional_arguments(a,b,c)

# keyword arguments
positional_arguments(ram=a,shyam=b,harish=c)

# default arguments
default_arguments(a)
