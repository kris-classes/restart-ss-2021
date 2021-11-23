"""
Password Strength Checker.

Features:
    - Password Length
    - Mixed-Case Passwords
    - Contains Numbers (Alphanumeric)
    - Contains Special Characters (Punctuation)
    - Checks if Too Common (Against a common passwords list)
"""



# Ask for the password

password = input("Please enter your password: ")

# Get the length
password_length = len(password)


# Check the length
if password_length < 12:  # TODO: Change from hardcoded value later.
    print("Your password is too short")

