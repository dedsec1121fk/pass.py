This Python script generates a random password each time it is run. Here’s a breakdown of what it does and how to use it:

### What it Does:
1. **Imports**: It imports necessary modules (`random` for generating random values and `string` for predefined character sets).
   
2. **Function Definition (`generate_password`)**:
   - Defines character sets:
     - `string.ascii_lowercase`: Lowercase letters (a-z)
     - `string.ascii_uppercase`: Uppercase letters (A-Z)
     - `string.digits`: Digits (0-9)
     - `string.punctuation`: Special characters (like !, @, #, etc.)
   
   - Generates:
     - `first_char`: Random first alphabetical character.
     - `last_char`: Random last alphabetical character (ensures it’s different from `first_char`).
     - `middle_chars`: Random sequence of characters of length between 6 to 10, chosen from all defined character sets.
   
   - Constructs the password by concatenating `first_char`, `middle_chars`, and `last_char`.
   
   - Shuffles the characters of the password to add randomness.

3. **Main Program (`__name__ == "__main__"`)**:
   - Calls `generate_password()` to get a random password.
   - Prints the generated password.

### How to Use It:
1. **Setup**:
   - Ensure Python is installed on your system. This script is designed to work with Python 3.

2. **Running the Script**:
   - Save the script to a file, e.g., `generate_password.py`.
   - Run the script using Python in a terminal or command prompt:
     ```
     python generate_password.py
     ```

3. **Output**:
   - Each time you run the script, it will print a newly generated random password.

### Example Output:
For example, running the script might output:
```
Generated Password: D4!phsNwUy
```

### Notes:
- The password length will vary between 8 to 12 characters due to the random length of `middle_chars` (6 to 10 characters) plus `first_char` and `last_char`.
- It ensures that the first and last characters are different to enhance password strength.
- The password includes a mix of uppercase letters, lowercase letters, digits, and special characters, making it suitable for many security requirements.

This script is handy for generating secure passwords quickly whenever you need one.
