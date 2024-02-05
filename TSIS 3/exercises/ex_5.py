# lCreate a bank account class that has attributes owner, balance and two methods deposit and withdraw.
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, 
# and test to make sure the account can't be overdrawn.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal rejected.")


account = BankAccount("John Doe")


account.deposit(1000)
account.deposit(500)


account.withdraw(200)
account.withdraw(1000)

account.withdraw(800)


print(f"Final balance for {account.owner}: {account.balance}")
