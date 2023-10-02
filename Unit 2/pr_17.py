# write a program to create nested list and display its elements

# creating nested list
nest_list = [['a', 'b', 'c'],[1, 2, 3], ["jaymin", "kishan", "het"]]

# display list
print(nest_list)

# display list another way
for i in nest_list:
    print(" ".join(map(str, i)))