class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = bool(checking_account)


    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError()
        self.balance -= amount
        return f"{self.name} has {self.balance}."


    def check(self, other_user, amount):
        if other_user.checking_account == False or other_user.balance < amount:
            raise ValueError()
        self.balance += amount
        return f"{self.name} has {self.balance} and {other_user.withdraw(amount)}"


    def add_cash(self, amount):
        self.balance += amount
        return f"{self.name} has {self.balance}."
