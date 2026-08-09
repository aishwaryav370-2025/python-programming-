import random

songs = {
    "happy": [
        "Uptown Funk - Bruno Mars",
        "Happy - Pharrell Williams",
        "On Top of the World - Imagine Dragons"
    ],
    "sad": [
        "Let Her Go - Passenger",
        "Someone You Loved - Lewis Capaldi",
        "Lovely - Billie Eilish"
    ],
    "angry": [
        "Believer - Imagine Dragons",
        "Numb - Linkin Park",
        "Warriors - Imagine Dragons"
    ],
    "relaxed": [
        "Perfect - Ed Sheeran",
        "Until I Found You - Stephen Sanchez",
        "Photograph - Ed Sheeran"
    ],
    "energetic": [
        "Don't Start Now - Dua Lipa",
        "Levitating - Dua Lipa",
        "On My Way - Alan Walker"
    ]
}

print("=" * 45)
print("       🎵 MOOD-BASED MUSIC RECOMMENDER")
print("=" * 45)

print("\nAvailable moods:")
for mood in songs:
    print("•", mood.capitalize())

mood = input("\nHow are you feeling today? ").lower().strip()

if mood in songs:
    print("\n🎧 Recommended songs for your mood:")
    recommendations = random.sample(songs[mood], 2)

    for number, song in enumerate(recommendations, 1):
        print(f"{number}. {song}")

    print("\n✨ Hope these songs match your vibe!")
else:
    print("\n❌ Sorry, I don't recognize that mood.")
    print("Try: happy, sad, angry, relaxed, or energetic.")