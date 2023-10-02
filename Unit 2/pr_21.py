# write a program to convert the elements of two list to key:value pairs of a dictionary.

# list 1
keys = [1,2,3,4]
values = ['a', 'b', 'c', 'd']

new_dict = dict(zip(keys,values))
print(new_dict)