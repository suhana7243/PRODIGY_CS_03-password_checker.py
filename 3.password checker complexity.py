def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if any(char in "!@#$%^&*()-_+=<>?/{}[]|" for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$...).")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, feedback


password = input("Enter your password: ")
strength, score, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
print(f"Score: {score}/5")

if strength != "Strong":
    print("Feedback to improve your password:")
    for tip in feedback:
        print("-", tip)
else:
    print("Great job! Your password is strong and secure.")
