print("🕵️ DETECTIVE MYSTERY")
print("=" * 30)

print("\nA diamond has been stolen from a mansion!")
print("There are 3 suspects:")
print("1. Alex")
print("2. Rahul")
print("3. John")

print("\nYou found three clues:")
print("🔎 Clue 1: The thief left a muddy footprint.")
print("🔎 Clue 2: The thief knew the secret room.")
print("🔎 Clue 3: The thief was wearing black shoes.")

choice = input("\nWho do you think is the thief? ")

if choice.lower() == "rahul":
    print("\n🎉 Congratulations!")
    print("You solved the mystery!")
    print("Rahul was the thief.")
else:
    print("\n❌ Wrong suspect!")
    print("The real thief was Rahul.")

print("\nCase Closed! 🔐")