print("😊 MINI MOOD DETECTOR 😊")

mood = input("How are you feeling today? ").lower()

if "happy" in mood or "good" in mood or "great" in mood:
    print("✨ That's amazing! Keep smiling!")
elif "sad" in mood or "bad" in mood or "upset" in mood:
    print("💙 It's okay to have bad days. Tomorrow can be better!")
elif "angry" in mood or "mad" in mood:
    print("😌 Take a deep breath and give yourself some time.")
elif "tired" in mood or "sleepy" in mood:
    print("😴 You need some rest. Take care of yourself!")
elif "excited" in mood:
    print("🔥 That's great! Enjoy the moment!")
else:
    print("🌸 Whatever you're feeling, take it one step at a time.")

print("Have a wonderful day! 🌷")