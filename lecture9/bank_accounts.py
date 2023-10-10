class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name

        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}.")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f} dollars")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.get_balance()

    def withdraw(self, amount):
        self.balance -= amount
