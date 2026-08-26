print("🌈 Welcome to MoodMate!")
name = input("What is your name? ")
mood = input("How are you feeling today? ").lower()

print(f"\nHello {name}! Let's see what MoodMate suggests.")

if mood in ["happy", "excited", "good"]:
    print("✨ Keep that positive energy!")
    print("🎵 Listen to your favorite song.")
    print("📸 Capture a happy moment today.")

elif mood in ["sad", "upset", "low"]:
    print("💙 It's okay to feel this way.")
    print("🌿 Take a short walk and breathe deeply.")
    print("💬 Talk to someone you trust.")

elif mood in ["angry", "frustrated"]:
    print("😌 Take a few deep breaths.")
    print("🧘 Give yourself some quiet time.")
    print("💡 Solve the problem when you feel calmer.")

else:
    print("🤔 Interesting mood!")
    print("☕ Take a small break.")
    print("🌟 Do one thing that makes you happy.")

print(f"\nGoodbye {name}! Remember: every day is a new chance! ❤️")