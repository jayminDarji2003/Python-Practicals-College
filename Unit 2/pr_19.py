# create a program to sort tuple with nested tuples

tup = ((1,(2,3)), (3,(2,1), (2,(2,1))))

# original
print(tup)
print(type(tup))

SORTED_TUPLE = sorted(tup, key=lambda t: (t[1][1],t[0]))

# sorted
print(tup)
print(type(tup))