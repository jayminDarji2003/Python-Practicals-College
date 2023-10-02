# write a program to generate prime numbers with the help of a function to test prime or not

# fnx that checks prime or not
def test_prime(num):
    if num > 1:
        for i in range(2,num):
            if i % 2 == 0:
                print(num, "Not a prime number")
                break
            else:
                print(num, "Prime number")
    else:
        print(num, "Not prime number")

number = int(input("Enter number to check prime or not : "))
test_prime(number)
