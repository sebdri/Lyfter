class BankAccount:
    balance = 0 


    def add_balance(self, amount):
        self.balance+=amount

    def withdraw_balance(self, amount):
        self.balance-=amount