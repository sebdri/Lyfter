class BankAccount:
    def __init__(self, owner , balance):
        if balance<=0:
            raise ValueError("The initial balance cannot be negative")

        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("The amount to deposit cannot negative")

        self.balance += amount


    def withdraw(self, amount):
        if amount <= 0 :
            raise ValueError ("The withdrawal amount must be greater than zero")

        if self.balance < amount:
            raise ValueError ("Insufficient funds")

        self.balance-=amount


    def show_balance(self):
        return self.balance

# ---<INTERACTIVE PART>---

#creating the account
while True:
    try:
        owner = input("Enter your name: ")
        initial_balance = float(input("Enter your initial balance: "))
        account = BankAccount(owner, initial_balance)

        break

    except ValueError as error:
        print (error)


# ---<MENU>---

#Creating the menu 


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
        amount = float(input("Please enter the amount to deposit: "))
        account.deposit(amount)

    elif option == "2":
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif option == "3":
        print(f'You current balance is: {account.show_balance()}') 
    elif option == "4":
        print("You are exiting your bank account \n" \
        "Bye Bye")
        break
    else:
        print("Invalid option.")