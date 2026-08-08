class BankAccount:
    def __init__(self):
        self.balance = 0 


    def add_balance(self, amount):
            self.balance+=amount
    
    def withdraw_balance(self, amount):

        while True:
            
            if self.balance > amount:
                self.balance-=amount
            else:

                raise ValueError ("Inavlid operation")

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
        


    def withdraw_balance(self, amount):

        if amount < min_balance:
            raise ValueError ("Invalid process")


        
        
    
