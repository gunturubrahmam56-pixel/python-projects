import random
import string

# Ask user for password length
length = int(input("Enter the password length: "))

# Combine all characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

# Generate password
password = "".join(random.choice(all_characters) for i in range(length))

print("Generated Password:", password)
