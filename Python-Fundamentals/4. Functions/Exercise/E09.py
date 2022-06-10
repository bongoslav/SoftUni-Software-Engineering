import re

def valid_password(password: str):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    # without RegEx:
    for char in password:
        if not 57 >= ord(char) >= 48 and not 90 >= ord(char) >= 65 and not 122 >= ord(char) >= 97:
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    nums_list = []
    for char in password:
        if 57 >= ord(char) >= 48:
            nums_list.append(char)
    if len(nums_list) < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()
valid_password(password)