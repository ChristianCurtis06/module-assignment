# Task 1: Custom Module with Aliases
# Importing 'text_utils' module via alias 'tu'
import text_utils as tu

# Creating user interface that utilizes the 'text_utils' functions to manipulate the string input
print("String Manipulation Program")
while True:
    print("\n1. Reverse a string\n2. Capitalize a string\n3. Quit")
    user_input = input("Enter your choice: ")
    if user_input == '1':
        string_input = input("Enter a string to reverse: ").strip()
        reversed_string = tu.reverse_string(string_input)
        print(f"Reversed string: '{reversed_string}'")
    elif user_input == '2':
        string_input = input("Enter a string to capitalize: ").strip()
        capitalized_string = tu.capitalize_string(string_input)
        print(f"Capitalized string: '{capitalized_string}'")
    elif user_input == '3':
        print("Quitting the program...")
        break
    else:
        print("Invalid input. Please try again.")