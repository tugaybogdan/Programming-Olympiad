import re

def is_valid_password(password):
    if not 8 <= len(password) <= 12:
        return False

    if not re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])", password):
        return False
    return True

password = input("Print password: ")

if is_valid_password(password):
    print("Valid")
else:
    print("Invalid")