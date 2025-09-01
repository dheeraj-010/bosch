class Bankaccount:
    def __init__(self,acc_num,acc_holder,account_bal):
        self.account_bal=0.0
        self.acc_num=acc_num
        self.acc_holder=acc_holder


    def deposit(self,amount):
        self.account_bal+=amount
    
    def withdraw(self,amount):
        if amount>self.account_bal:
            print("account balance insufficient ")
            exit
        else:
            self.account_bal-=amount
    
    def  get_balance(self):
        print("The balance is :" , self.account_bal)

    def __str__(self):
        return f"{self.acc_holder} with account no {self.acc_num} has balance {self.account_bal}"

class SavingsAccount(Bankaccount):
    def __init__(self, bank_account_obj,):
        super().__init__(bank_account_obj.acc_num, bank_account_obj.acc_holder, bank_account_obj.account_bal)

    def apply_interest(self,interest_rate):
        interest = (self.account_bal * interest_rate/100)
        self.account_bal += interest
        print(f"Interest of {interest} applied. New balance: {self.account_bal}")



person1=Bankaccount(1234,"Dheeraj",0)
savings=SavingsAccount(person1)
savings.deposit(1000)
savings.get_balance()
savings.apply_interest(5)
savings.get_balance()
