```python
import random

print("🔮 DIGITAL FORTUNE TELLER 🔮")
print("-" * 30)

name = input("Enter your name: ")
question = input("Ask me a yes/no question: ")

answers = [
    "✨ Definitely YES!",
    "🌟 Most likely YES!",
    "😊 Yes, but be patient.",
    "🤔 Maybe...",
    "😐 Hard to say right now.",
    "⚠️ Probably NOT.",
    "❌ Definitely NO!",
    "🌈 Ask again later!"
]

print("\nThinking... 🔮")
print(f"\n{name}, your fortune says:")
print(random.choice(answers))
```
