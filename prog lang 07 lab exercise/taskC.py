import re

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter"
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    if not re.search(r"\d", password):
        return "Password must contain at least one number"
    if not re.search(r"[!@#$%^&*()',.?\:{}|<>]", password):
        return "Password must contain at least one special character"

    return None

while True:
    password = input("Enter your password (must contain at least one lowercase letter, one uppercase letter, one number, and one symbol): ")
    error_message = validate_password(password)
    
    if error_message:
        print(error_message)
        print("Please try again.\n")
    else:
        print("Password is valid!")
        break
