expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"Item": item, "Amount": amount})
        print("Expense Added Successfully!")

    elif choice == "2":
        if expenses:
            print("\nExpense List")
            for expense in expenses:
                print(f"{expense['Item']} - ₹{expense['Amount']}")
        else:
            print("No expenses found.")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["Amount"]
        print("Total Expense: ₹", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")