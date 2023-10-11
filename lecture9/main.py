from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.withdraw(15000)

Dave.transfer(1000, Sara)

Jim = InterestRewardsAccount(1000, "Jim")

Jim.deposit(1000)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(1000, Sara)
