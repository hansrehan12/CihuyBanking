
# this my first time to build a code from python, and thanks to  Youtube 'Bro Code' that i learn from here.
def show_balance(balance):
    print(f"Your Balance is Rp.{balance:.2f}")

def deposit():
    amount = float(input("input your amount to deposit :"))

    if amount < 0:
        print("that's not valid amount!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter Amount to be Withdraw : "))

    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    

balance = 0
is_running = True

while is_running :
    print("***********************")
    print("Welcome To CihuyBANK!")
    print("***********************")
    print("banking Program")
    print("***********************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your Choice 1-4 : ")
    
    if choice == '1':
        show_balance(balance)
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw(balance)
    elif choice == '4':
        is_running = False
    else:
        print("not valid a choice")        

print("ThankYou for using CihuyBANK!")

