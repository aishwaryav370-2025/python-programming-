```python
import random

compliments = [
    "✨ You have amazing energy!",
    "🌟 You make things better just by being there!",
    "💫 You are doing better than you think!",
    "🔥 Your confidence is your superpower!",
    "🌈 You have a unique personality!",
    "🚀 Keep going, you're getting closer!",
    "💖 You deserve good things!"
]

print("💬 RANDOM COMPLIMENT GENERATOR")
print("--------------------------------")

name = input("Enter your name: ")

compliment = random.choice(compliments)

print("\nHey", name + "!")
print(compliment)
print("Have a wonderful day! 😊")
```
