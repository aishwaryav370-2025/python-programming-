import random

name = input("Enter your name: ")

dreams = [
    "Future Tech Innovator 🚀",
    "Creative Explorer 🎨",
    "Code Wizard 💻",
    "Brilliant Problem Solver 🧠",
    "Adventure Seeker 🌍",
    "AI Mastermind 🤖",
    "Digital Artist ✨",
    "Future Entrepreneur 💼"
]

powers = [
    "creativity",
    "confidence",
    "curiosity",
    "intelligence",
    "leadership",
    "imagination"
]

print("\n✨ DREAM PROFILE ✨")
print("Name:", name.title())
print("Dream Role:", random.choice(dreams))
print("Special Power:", random.choice(powers).title())
print("Lucky Number:", random.randint(1, 100))
print("\nKeep dreaming,", name.title(), "🌟")