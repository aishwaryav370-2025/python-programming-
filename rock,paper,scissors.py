import random

print("🎮 Rock, Paper, Scissors Game")

choices = ["rock", "paper", "scissors"]

while True:
    player = input("\nEnter rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie! 🤝")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("🎉 You win!")

    else:
        print("😔 Computer wins!")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing! 👋")
        break
    
    
    