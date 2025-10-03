"""
Python Learning Journal: Chapter 2 - If-Else and Flow Control.

Focus: Conditional logic, boolean operations, comparison operators, and basic error handling.
Demonstrates: if/elif/else structure, the try/except block, string methods, and best practices
for constants (UPPER_SNAKE_CASE).
"""

# CONSTANTS (Best Practice: Use UPPER_SNAKE_CASE for values that should not change)
PASSWORD = 'mellon'
FELLOWSHIP_COUNT = 9


def gate_riddle():
    """Manages the two-part riddle sequence using flow control."""

    # 1. Primary Flow Control (Password Check)
    password_input = input('What say you at the gates of Moria?\n> ').lower()

    if password_input == PASSWORD:
        print('Greetings, friend of Moria, you may enter our hallowed halls.')

    elif password_input == 'bellon':
        print('I may have misheard you, try again Mr McKellen.')

    elif password_input == 'join the dark lord and be spared his wroth':
        print('You are no friend of ours, away with you!')

    # 2. Secondary Flow Control (Riddle Check, nested in the final ELSE)
    else:
        print('You know not the password. You must answer a different riddle to prove your friendship.')

        fellowship_answer = input('How many set off from Rivendell as the Fellowship?\n> ')

        # 3. Error Handling (try/except) and Type Conversion
        try:
            # Convert string input to integer for comparison (int() is necessary here)
            fellowship_count = int(fellowship_answer)

            # Nested Flow Control: Compare the numeric answer to the constant
            if fellowship_count == FELLOWSHIP_COUNT:
                print('You are indeed a friend or a well-informed spy. One more riddle you shall face.')

            elif 1 < fellowship_count < 9:
                # Example of Boolean Logic (AND operator is implicit in a chained comparison)
                print(f'That\'s close, but short. The fellowship must be stronger!')

            elif fellowship_count >= 100:
                print('Wouldn\'t that be nice! Assuming you were joking, what was the real strength of the fellowship?')

            else:
                print('You have failed the test, there is no hope for you. Begone!')

        # 4. ValueError Catch: Handles non-numeric answers (e.g., 'nine')
        except ValueError:
            print(f'I am searching for an exact number, try again. The gates remain shut.')


# Execute the main function to run the script
gate_riddle()

# End of Chapter 2 - If-Else and Flow Control
