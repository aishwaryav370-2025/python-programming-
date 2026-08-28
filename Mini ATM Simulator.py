balance = 5000

print("===== MINI ATM =====")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        balance += amount
        print("Money deposited successfully!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= balance:
            balance -= amount
            print("Please collect your cash.")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice!")