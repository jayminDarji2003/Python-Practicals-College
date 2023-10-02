'''
    Create sample list of 7 elements and implement the list methods.
        1. append
        2. insert
        3. copy
        4. extend
        5. cound
        6. pop
        7. sort
        8. reverse
        9. clear
'''

sample_list = [i for i in range(0,8)]

# print list
print("Our list looks like : " , sample_list)

# append
sample_list.append(1000)
print(sample_list)

# insert 
sample_list.insert(0,90890)
print(sample_list)

# copy
new_list = sample_list.copy()
print(new_list)

# extend
extra_list = [i for i in range(10,15)]
sample_list.extend(extra_list)
print(sample_list)

# count
ans = sample_list.count(5)
print(ans)

# pop
print(sample_list.pop())
print(sample_list)

# sort
sample_list.sort()
print(sample_list)

# reverse
sample_list.reverse()
print(sample_list)

# clear
sample_list.clear()
print(sample_list)