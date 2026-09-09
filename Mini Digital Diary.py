from datetime import datetime

print("📔 MINI DIGITAL DIARY")
print("----------------------")

while True:
    print("\n1. Write a diary entry")
    print("2. View diary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("Write your thoughts: ")
        time = datetime.now().strftime("%d-%m-%Y %H:%M")

        with open("diary.txt", "a") as file:
            file.write(f"\n[{time}]\n{entry}\n")

        print("✅ Entry saved successfully!")

    elif choice == "2":
        try:
            with open("diary.txt", "r") as file:
                content = file.read()

            if content:
                print("\n📖 YOUR DIARY")
                print(content)
            else:
                print("Your diary is empty.")

        except FileNotFoundError:
            print("No diary entries found.")

    elif choice == "3":
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")