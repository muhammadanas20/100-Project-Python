class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0: 
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance: 
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(("withdrawal", amount))
     

account = BankAccount("Student",5000)
account.deposit(700)
account.withdraw(1000)
print(f"Balance: {account.balance:.2f} rupees")
print(account.history)