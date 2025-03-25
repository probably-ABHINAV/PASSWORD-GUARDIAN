import string
import re

common_weak_passwords = ["123456", "123456789", "111111", "654321", "123123", 
    "12345678", "1234567", "112233", "qwerty", "qwerty123",
    "qwertyuiop", "1qaz2wsx", "asdfgh", "zxcvbn", "password",
    "admin", "welcome", "login", "letmein", "sunshine",
    "iloveyou", "monkey", "football", "master", "hello",
    "superman", "!@#$%^&*", "1q2w3e4r", "qweasd", "abc123",
    "password1", "admin123", "01011980", "121212", "102030",
    "2023", "2024", "starwars", "pokemon", "snoopy",
    "batman", "harrypotter", "p@ssw0rd", "adm1n", "passw0rd",
    "h3llo", "w3lcome", "krishna", "ganesha", "sairam",
    "jaihind", "namaste", "swastik", "bharat", "maa",
    "omnamahshivaya", "sachin", "aishwarya", "sonu", "rani",
    "mumbai", "delhi", "chennai", "kolkata", "india",
    "hindustan", "15081947", "26011950", "02042020", "9999999999",
    "1234567890", "iloveindia", "test123", "admin@123", "user123",
    "namaste123", "india123", "iplt20", "cricket", "dhoni",
    "kohli", "srk", "salman", "password123", "india2023",
    "jaihind1", "a1b2c3d4"]

def evaluate_password_strength(password):
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1

    if re.search(r'[0-9]', password):
        score += 1

    if re.search(r'[^A-Za-z0-9]', password):
        score += 1

    if len(set(password)) == len(password):
        score += 1

    return score

def detect_weakness(password):
    if password.lower() in common_weak_passwords:
        return "🚨 Yikes! This password is on every hacker's top 10 list. Let's get more creative!"

    dictionary_words = ['password', 'admin', 'user', 'welcome', 'love', 'secret']
    for word in dictionary_words:
        if word in password.lower():
            return f"🔍 Psst... '{word}' is too obvious. Let's avoid dictionary words!"
    
    if re.search(r'(.)\1\1', password):
        return "🔄 Repeated characters alert! Mix it up like a good playlist."
    elif re.search(r'0123456789', password):
        return "🔢 Simple sequences are like candy to hackers. Break the pattern!"

    return "🌟 No obvious weaknesses found! But let's check recommendations..."

def provide_recommendations(password):
    recommendations = []

    if len(password) < 12:
        recommendations.append("📏 Make it longer! Aim for at least 12 characters - like a mini story for security")
    if not re.search(r'[A-Z]', password):
        recommendations.append("🆙 Spice it up with CAPITAL LETTERS - they're like security guards")
    if not re.search(r'[a-z]', password):
        recommendations.append("🔤 Add some lowercase letters for better flow")
    if not re.search(r'[0-9]', password):
        recommendations.append("🔢 Numbers aren't just for math - sprinkle a few in!")
    if not re.search(r'[^A-Za-z0-9]', password):
        recommendations.append("🎉 Party time! Add special characters like ! or & to really shine")
    
    return recommendations

print("\n🔒 Welcome to the Password Coach! Let's make your digital fortress stronger together 💪")

while True:
    password = input("\n🗝 Enter your password (or 'exit' to quit): ")
    if password.lower() == 'exit':
        print("\n👋 Stay secure out there! Happy password crafting!")
        break

    score = evaluate_password_strength(password)

    print("\n🔍 Analyzing your password...")
    
    strength_feedback = {
        0: "☠  Danger zone! This is a master key for hackers",
        1: "🛑 Super fragile! Let's build some defenses",
        2: "⚠  Shaky ground! Time for reinforcements",
        3: "🟡 Not bad! But we can level up",
        4: "🟢 Solid start! Let's make it legendary",
        5: "💎 Now we're talking! But perfection takes work",
        6: "🎖  Security champion! You're crushing it!"
    }
    
    print(f"\n{strength_feedback.get(min(score, 6), '🌀 Hmm...')}")
    
    weakness = detect_weakness(password)
    print(f"\n{weakness}")

    recommendations = provide_recommendations(password)
    if recommendations:
        print("\n💡 Pro tips to level up:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    else:
        print("\n🌈 Perfect! This password could survive a zombie apocalypse!")

    print("\n👉 Remember: Great passwords are like good stories - unique, memorable, and hard to predict!")
