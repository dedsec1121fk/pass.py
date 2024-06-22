#!/data/data/com.termux/files/usr/bin/python

import random
import string

def generate_password():
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Generate first and last alphabetical characters
    first_char = random.choice(string.ascii_letters)
    last_char = random.choice(string.ascii_letters)
    
    # Ensure they are different to avoid starting and ending with the same character
    while first_char == last_char:
        last_char = random.choice(string.ascii_letters)
    
    # Generate middle characters (length between 6 to 10 characters)
    length = random.randint(6, 10)
    middle_chars = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    
    # Concatenate and shuffle the password
    password = first_char + middle_chars + last_char
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)