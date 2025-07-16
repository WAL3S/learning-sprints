class BankAcount:
    def __init__(self, intital_balance=0):
        self.balance = intital_balance
    
    def deposit(self, amount):
        self.balance=amount+self.balance
        print(f'Deposited {amount}, current balance: {self.balance}')
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print(f"Withdrawed {amount}, current balance {self.balance}")
            
        else:
            print("You can only withdraw as much or less than your current balance")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def check_for_proper_input(prompt):
   while True:
        try:
            user_input = input(prompt).strip()
            return float(user_input)
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    acount_1=BankAcount()

    while True:
        print("\nWhat would you like to do?")
        print("  1) Deposit")
        print("  2) Withdraw")
        print("  3) Check balance")
        print("  Q) Quit")
        choice = input("Enter choice: ").strip().lower()

        if choice=='1':
            cash=check_for_proper_input("Enter amount to deposit: ")
            acount_1.deposit(cash)
        elif choice=='2':
            cash=check_for_proper_input("how much would you like to withdraw: ")
            acount_1.withdraw(cash)
        elif choice=='3':
            acount_1.check_balance()
        elif choice=='q':
            print("See you next time!")
            break
        else:
            print("Please enter 1, 2, 3, or Q.")

if __name__ =="__main__":
    main()
        
