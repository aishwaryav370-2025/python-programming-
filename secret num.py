import random

print("🔮 Secret Number Personality Test")
name = input("Enter your name: ")

number = random.randint(1, 9)
print("\nChoose a number from 1 to 9")
choice = int(input("Your choice: "))

if choice == number:
    print("🎉 Amazing! You matched the secret number!")
elif choice > number:
    print("⬇️ Your number is higher than the secret number.")
else:
    print("⬆️ Your number is lower than the secret number.")

print("\n✨ Your personality result:")
if choice % 2 == 0:
    print("You are calm, balanced and thoughtful!")
else:
    print("You are energetic, creative and adventurous!")

print(f"\n{name}, your secret number was {number}!")
print("Thanks for playing! 🌟")