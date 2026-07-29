

class BankAccount:
    def __init__(self, owner, balance):
        if balance<0:
            raise ValueError("The initial balance cannot be negative.")

        self.owner = owner
        self.balance = balance



    def deposit_amount(self, amount):
        if amount <= 0:
            raise ValueError("The amount to deposit cannot negative")


        self.balance += amount


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError ("Insufficient funds.")


        self.balance -= amount

    def show_balance(self):
        return self.balance


while True:
    try:

        owner = input("Enter  your name: ")
        initial_balance = float(input("Enter the initial balance: "))
        account = BankAccount(owner,initial_balance)


        break
    except ValueError as error:
        print(error)


def menu():
    print("\n===== BANK ACCOUNT =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

while True:
    menu()
    option = input("Choose an option: ")

    if option == "1":
        amount = float(input("Enter the amount to deposit: "))
        account.deposit_amount(amount)

    elif option == "2":
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif option == "3":
        print(f'You current balance is: {account.show_balance()}') 
    elif option == "4":
        break
    else:
        print("Invalid option.")