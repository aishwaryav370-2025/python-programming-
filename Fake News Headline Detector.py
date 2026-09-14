headline = input("Enter a news headline: ").lower()

suspicious_words = [
    "shocking", "secret", "100% true",
    "you won't believe", "breaking",
    "miracle", "guaranteed"
]

found = []

for word in suspicious_words:
    if word in headline:
        found.append(word)

print("\n🔎 Checking headline...")

if found:
    print("⚠️ This headline may be clickbait!")
    print("Suspicious words found:", ", ".join(found))
else:
    print("✅ No obvious clickbait words found.")

print("\nNote: This program only detects suspicious words; "
      "it cannot confirm whether news is actually true.")