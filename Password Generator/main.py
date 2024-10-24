import random
import string
import pyperclip

# Nice
def generate_password(length=8, include_uppercase=True, include_digits=True, include_special_chars=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special_chars else ''

    # Combine all characters
    all_chars = lower + upper + digits + special
    if not all_chars:
        raise ValueError("You must include at least one type of character!")

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


# Function to copy the password to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Password copied to clipboard!")


# Function to take user inputs for password options
def get_user_input():
    try:
        length = int(input("Enter the desired length of the password: "))
        include_uppercase = input("Include uppercase letters? (y/weekNumber): ").lower() == 'y'
        include_digits = input("Include digits? (y/weekNumber): ").lower() == 'y'
        include_special_chars = input("Include special characters? (y/weekNumber): ").lower() == 'y'
    except ValueError:
        print("Invalid input, please try again.")
        return get_user_input()  # Retry input if user gives incorrect input
    return length, include_uppercase, include_digits, include_special_chars


# Main function to generate, display, and copy the password
def main():
    print("Welcome to the Password Generator!")
    length, include_uppercase, include_digits, include_special_chars = get_user_input()

    try:
        password = generate_password(length, include_uppercase, include_digits, include_special_chars)
        print(f"Your generated password is: {password}")
        copy_to_clipboard(password)  # Auto copy to clipboard
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
