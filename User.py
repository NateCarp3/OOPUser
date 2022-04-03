from unicodedata import name


class User:		# here's what we have so far
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):	# takes an argument that is the amount of the withdrawal
        self.account_balance -= amount	# the specific user's account decreases by the amount of the value received


User(name)
Nate = User("Nate")
Nizzy = User("Nizzy")
Ric = User("Ric")
# Accessing the instance's attributes
Nate.make_deposit(100)
Nate.make_deposit(50)
Nate.make_deposit(60)
Nate.make_withdrawal(5)
Nizzy.make_deposit(100)
Nizzy.make_deposit(90)
Nizzy.make_withdrawal(30)
Nizzy.make_withdrawal(10)
Ric.make_deposit(40)
Ric.make_withdrawal(4)
Ric.make_withdrawal(11)
Ric.make_withdrawal(5)


print(Nate.name, Nate.account_balance)
print(Nizzy.name, Nizzy.account_balance)
print(Ric.name, Ric.account_balance)






