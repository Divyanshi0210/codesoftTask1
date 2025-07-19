# Developed by: Divyanshi Sharma
import random
import string
import time

def show_title():
    print("*+" * 50)
    print("                     PASSWORD GENERATOR")
    print("+*" * 50)

def get_length():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Password length must be at least 6.")
            else:
                return length
        except:
            print("Invalid input. Please enter a valid number.")

def get_complexity():
    print("\nSelect password strength:")
    print("1. Weak (letters only)")
    print("2. Medium (letters and digits)")
    print("3. Strong (letters, digits, and symbols)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Please enter 1, 2, or 3.")

def generate_password(length, complexity):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if complexity == 1:
        characters = lowercase + uppercase
    elif complexity == 2:
        characters = lowercase + uppercase + digits
    else:
        characters = lowercase + uppercase + digits + symbols

    password = ''.join(random.choices(characters, k=length))
    return password

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(f"{time.ctime()} - {password}\n")
    print("Password saved to 'passwords.txt'.")

def main():
    show_title()

    while True:
        length = get_length()
        complexity = get_complexity()
        password = generate_password(length, complexity)

        print("\nGenerated Password:", password)

        save = input("Do you want to save this password? (yes/no): ")
        if save.lower() == 'yes':
            save_password(password)

        again = input("\nDo you want to generate another password? (yes/no): ")
        if again.lower() != 'yes':
            print("\nThank you for using the password generator.")
            break

if __name__ == "__main__":
    main()
