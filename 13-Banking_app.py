# Mevcut bakiyeyi ekrana yazdırır
def show_balance(balance):
    print(f"Your balance is €{balance:.2f}")

# Para yatırma fonksiyonu
def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("You cannot deposit a negative amount.")
        return 0
    else:
        return amount

# Para çekme fonksiyonu
def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    if amount < 0:
        print("You cannot withdraw a negative amount.")
        return 0
    elif amount > balance:
        print("Insufficient funds!")  # Çekilmek istenen miktar mevcut bakiyeden fazla
        return 0
    else:
        return amount

# Ana program başlıyor
balance = 0
is_running = True

while is_running:
    print("\n--- Banking Program ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_balance(balance)

    elif choice == '2':
        balance += deposit()

    elif choice == '3':
        balance -= withdraw(balance)

    elif choice == '4':
        is_running = False

    else:
        print("Invalid choice. Please select from 1 to 4.")

print("Thank you, have a nice day!")
