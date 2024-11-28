# import regular expressions
import re 

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return False
    # Check for uppercase and lowercase letters
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    # Check for digits
    if not any(char.isdigit() for char in password):
        return False
     # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True

def main():
    # Prompt user for password input
    print("Password Strength Checker")
    password = input("Enter your password: ")
    # Validate the password
    if check_password_strength(password):
        print("Strong password! ✅")
    else:
        print("Your password is weak !! Ensure it meets the following criteria:")
        print("- At least 8 characters long")
        print("- Contains both uppercase and lowercase letters")
        print("- Contains at least one digit (0-9)")
        print("- Contains at least one special character (e.g., !, @, #, $)")

if __name__ == "__main__":
    main()