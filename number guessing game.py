import random

print("🎮 Number Guessing Game")
print("I have chosen a number between 1 and 20.")

number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("🎉 Congratulations! You guessed it!")
        print("Number of attempts:", attempts)
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")