# create a Bank class with two variables name and balance. Implement a constructor to initialize the variables. Also implement deposit and withdraw using instance method.

class Bank:
    # constructor
    def __init__(self,name=None,balance=0):
        self.name = name
        self.balance = balance

    # getdata instance method
    def getData(self):
        print("--------------------------------")
        print("Name : ", self.name)
        print("Balance : ", self.balance)

    # Deposit instance method
    def deposit(self,amount):
        self.balance += amount

    # withdraw instance method
    def withdraw(self,amount):
        if amount > self.balance:
            print("Opps!!, you don't have enough balance to withdraw")
        else:
            self.balance -= amount

b = Bank("jaymin",10000)
b.getData()

b.withdraw(1000)
b.getData()

b.deposit(10000)
b.getData()

