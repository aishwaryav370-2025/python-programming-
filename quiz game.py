questions = {
    "What is the capital of India?": "Delhi",
    "How many days are there in a week?": "7",
    "Who developed Python?": "Guido van Rossum"
}

score = 0

for question, answer in questions.items():
    user = input(question + " ")
    if user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your Score:", score)