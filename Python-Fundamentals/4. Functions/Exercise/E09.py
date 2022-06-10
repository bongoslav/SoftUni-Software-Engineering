import re

def valid_password(password: str):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    # without RegEx:
    if password.isalnum():
        print("Password must consist only of letters and digits")

    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()
valid_password(password)