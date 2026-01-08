import random
import string

print("=== Random Password Generator ===")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        all_chars = letters + digits + symbols

        password = "".join(random.choice(all_chars) for _ in range(length))

        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
