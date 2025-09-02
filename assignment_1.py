class BankAccount:
    def __init__(self, acc_num, acc_holder, account_bal=1000.0):
        if account_bal < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_bal = account_bal
        self.acc_num = acc_num
        self.acc_holder = acc_holder

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.account_bal += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.account_bal:
            raise ValueError("Insufficient balance")
        self.account_bal -= amount

    def get_balance(self):
        print(f"The balance is: {self.account_bal}")
        return self.account_bal

    def __str__(self):
        return f"{self.acc_holder} with account no {self.acc_num} has balance {self.account_bal}"    


class SavingsAccount(BankAccount):
    def apply_interest(self, interest_rate):
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        interest = (self.account_bal * interest_rate / 100)
        self.account_bal += interest
        print(f"Interest of {interest} applied. New balance: {self.account_bal}")


class CurrentAccount(BankAccount):
    def __init__(self, acc_num, acc_holder, account_bal=0.0, overdraft_limit=0.0):
        super().__init__(acc_num, acc_holder, account_bal)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.account_bal + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit")
        self.account_bal -= amount
        print(f"{amount} withdrawn. New balance: {self.account_bal}")


class FixedDepositAccount(BankAccount):
    def __init__(self, acc_num, acc_holder, account_bal=0.0, lock_in_period=12):
        super().__init__(acc_num, acc_holder, account_bal)
        self.lock_in_period = lock_in_period  # in months
        self.locked = True

    def withdraw(self, amount):
        if self.locked:
            raise PermissionError("Funds are locked in Fixed Deposit account until maturity")
        super().withdraw(amount)

    def mature(self):
        self.locked = False
        print("Fixed Deposit account has matured. Funds can now be withdrawn.")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        if account.acc_num in self.accounts:
            raise ValueError("Account number already exists in the bank")
        self.accounts[account.acc_num] = account

    def transfer_funds(self, from_acc_num, to_acc_num, amount):
        if from_acc_num not in self.accounts or to_acc_num not in self.accounts:
            raise ValueError("Invalid account number(s)")
        sender = self.accounts[from_acc_num]
        receiver = self.accounts[to_acc_num]
        sender.withdraw(amount)
        receiver.deposit(amount)
        print(f"Transferred {amount} from {sender.acc_holder} to {receiver.acc_holder}")



if __name__ == "__main__":
    
    my_bank = Bank("Demo Bank")

   
    savings = SavingsAccount(1, "Dheeraj", 1000)
    current = CurrentAccount(2, "ramesh", 500, overdraft_limit=300)
    fd = FixedDepositAccount(3, "Sailesh", 2000, lock_in_period=12)

   
    my_bank.add_account(savings)
    my_bank.add_account(current)
    my_bank.add_account(fd)

   
    print("\n- Savings Account Test -")
    savings.deposit(500)
    savings.get_balance()
    savings.apply_interest(5)
    savings.get_balance()

   
    print("\nCurrent Account Test")
    current.withdraw(700)
    current.get_balance()
    try:
        current.withdraw(200)
    except ValueError as e:
        print("Error:", e)

    print("\nFD Test ")
    try:
        fd.withdraw(500) 
    except PermissionError as e:
        print("Error:", e)
    fd.mature()
    fd.withdraw(500) 
    fd.get_balance()

    print("\nTransfer Funds Test")

    my_bank.transfer_funds(1, 2, 3)
    savings.get_balance()
    current.get_balance()
