# create a decorator function to increase the value of function by 3.

def plus_one(num):
    def add_one(num):
        return num+3
    result = add_one(num)
    return result

ans = plus_one(10)
print(ans)