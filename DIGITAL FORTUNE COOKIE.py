import random

fortunes = {
    "study": [
        "Small progress every day becomes big success.",
        "Your future self will thank you for studying today.",
        "Don't memorize everything. Understand the concept."
    ],
    "career": [
        "Keep learning; your skills are your superpower.",
        "One good project can open a new door.",
        "Consistency beats talent when talent stops practicing."
    ],
    "life": [
        "Not every day has to be productive.",
        "Enjoy the journey, not only the destination.",
        "Sometimes a small step is enough."
    ]
}

print("🍪 DIGITAL FORTUNE COOKIE 🍪")
print("Categories: study | career | life")

choice = input("\nChoose your category: ").lower()

if choice in fortunes:
    print("\n✨ Your Fortune:")
    print(random.choice(fortunes[choice]))
else:
    print("Invalid category. Please choose study, career, or life.")