import random


def generate_password(length=12):
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit_chars = "0123456789"
    lower = random.choice(lower_chars)
    upper = random.choice(upper_chars)
    digit = random.choice(digit_chars)
    all_characters = lower_chars + upper_chars + digit_chars
    remaining_length = length - 3
    remaining = [random.choice(all_characters) for _ in range(remaining_length)]
    password_list = [lower, upper, digit] + remaining
    random.shuffle(password_list)

    return "".join(password_list)
user_length = int(input("Enter password length (minimum 4): "))
if user_length < 4:
    user_length = 4

new_password = generate_password(user_length)
print("Generated Password:", new_password)
