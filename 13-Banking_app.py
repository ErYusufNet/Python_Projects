def show_balance():
    print(f"Your balance is €{balance:.2f}")
def deposit():
    amount = float(input("enter an amount to be deposited: "))
    if amount < 0:
        print("You cannot deposit negative amount")
    else:
        return amount
def withdraw():
    pass

balance = 0
is_running = True
while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_balance()
    if choice == '2':
        balance += deposit()


    if choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice")
print("Thank you have a nice day!")

