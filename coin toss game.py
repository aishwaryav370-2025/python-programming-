import random

print("🪙 COIN TOSS GAME 🪙")

score = 0

while True:
    choice = input("\nChoose Heads or Tails (or type quit): ").lower()

    if choice == "quit":
        break

    if choice not in ["heads", "tails"]:
        print("❌ Invalid choice!")
        continue

    coin = random.choice(["heads", "tails"])

    print("The coin is:", coin)

    if choice == coin:
        print("🎉 You Win!")
        score += 1
    else:
        print("😢 You Lose!")

    print("Your score:", score)

print("\n🏆 Game Over!")
print("Final Score:", score)