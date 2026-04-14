import random
import string

def generate_password():
    print("\n--- PASSWORD GENERATOR ---")
    
    # User input for password length
    length = int(input("Enter desired password length: "))
    
    print("\nSelect password complexity:")
    print("1. Only letters")
    print("2. Letters + numbers")
    print("3. Letters + numbers + special characters")
    
    choice = input("Enter your choice (1/2/3): ")
    
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    if choice == '1':
        characters = letters
    elif choice == '2':
        characters = letters + digits
    elif choice == '3':
        characters = letters + digits + symbols
    else:
        print("Invalid choice!")
        return
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display result
    print("\nGenerated Password:", password)

# Run the program
generate_password()
