"""
Python Learning Journal: Chapter 5 - DEBUGGING.
File: debug_practice.py

Focus: Using Python's built-in tools to identify errors, enforce code assumptions,
       and record program execution flow.

Demonstrates:
- Raising Exceptions: Handling predictable critical errors (e.g., Division by Zero).
- Assertions: Enforcing assumptions about variable state and type before execution.
- Logging: Recording program events (DEBUG, INFO, WARNING, ERROR) for later review.
- Logging Levels: Customizing messages for different log severities.
- Modular code structure using functions (Call Stack).
"""

import sys, logging

# --- GLOBAL VARIABLES ---
# Initialized here, but they will be overwritten by user input later.
first_number = 1
second_number = 1


# --- LOGGING SETUP ---

# Sets the logging format and level. All messages at DEBUG level and above will be displayed.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program execution.')

# To save logs to a file instead of the console, uncomment the line below:
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# To disable all logging (for final release of the code), uncomment the line below:
# logging.disable(logging.CRITICAL)


# --- FUNCTION DEFINITIONS ---

def run_calculator_question_1():
    """Initial check to see if the user wants to play."""
    while True:
        user_choice = input(f'Care to try out this dinosaur?\n> ').lower()

        if user_choice == 'yes':
            print('I knew you were a good soul!\n')
            return True

        elif user_choice == 'no':
            print('Ah fair enough, I guess I understand.\nSee you soon, I hope!')
            sys.exit() # Exit the program

        else:
            print('A simple yes or no is required here, my friend.\n\nSo...', end='')
            continue


def calculator_input_validation():
    """Gets user input, validates it, and sets global variables."""
    global first_number, second_number

    # --- LOOP 1: Validate First Number ---

    logging.debug('Starting Loop 1 for first number input.')

    while True:
        try:
            first_num_str = input(f'First, enter the number you want divided.\n> ')
            first_number = int(first_num_str)

            # If successful, break out of this loop.
            break

        except ValueError:
            # Handle non-numeric input for the first number
            logging.warning('User entered non-integer value for first number.')
            print("Please enter only whole numbers (integers) for the first number. Try again, you old maverick!")
            continue # Restarts Loop 1

    # --- LOOP 2: Validate Second Number (Nested Loop) ---

    logging.debug('Starting Loop 2 for second number input validation.')

    while True:
        try:
            second_num_str = input(f'Now enter the number you want to divide it by.\n> ')
            second_number = int(second_num_str)

            # --- RAISING EXCEPTIONS ---
            if second_number == 0:
                # Log the error before raising the exception
                logging.error('Attempted input of zero for the divisor. Raising exception.')

                # Raise a specific exception to halt the function and report the problem
                raise Exception("This number can't be zero, it would break the mathmatical world!")

            # If successful, break out of this inner loop.
            break

        except ValueError:
            # Handle non-numeric input for the second number
            logging.warning('User entered non-integer value for second number.')
            print("Please enter only whole numbers (integers) for the second number. Try again, you old maverick!")
            continue # Restarts Loop 2

        except Exception as e:
            # This handles the specific exception raised for the zero input
            print(f"Error Caught: {e}")
            continue # Restarts Loop 2, prompting for a new second number

    # If the function reaches this point, both inputs are valid and assigned globally.
    logging.info('User successfully validated input numbers.')
    return True


def division_calculation():
    """Performs the division (Highlighting logging and assertions)."""
    global first_number, second_number

    # --- ASSERTIONS ---
    # Assertions check the precondition: Ensure the variables are integers before division.
    assert isinstance(first_number, int), 'Assertion Failed: First number must be an integer.'
    assert isinstance(second_number, int), 'Assertion Failed: Second number must be an integer.'

    # Log the values being used before calculation
    logging.debug(f'Starting division: {first_number} / {second_number}')

    # We use a try/except block here to safely handle any division errors
    try:
        # The '//' operator performs integer division (no decimal part)
        division_answer = first_number // second_number

        # Log success
        logging.info(f'SUCCESS: {first_number} / {second_number} resulted in {division_answer}.')

        # Correctly print the calculated answer
        print(f'\nThis old dinosaur calculator says that {first_number} / {second_number} = {division_answer}')

        return True # Return success

    except ZeroDivisionError:
        # Log the critical error (should ideally not be reached due to validation)
        logging.critical('ZeroDivisionError: Calculation attempted after validation failure.')

        # This will catch the error if it somehow slipped past validation
        print("\nFATAL ERROR: Division by zero occurred! Something went wrong in validation.")
        return False # Return failure


def run_calculator_question_2():
    """Asks if the user wants to run another calculation."""
    logging.info('Program will attempt next calculation.')
    print(f'\nNot bad for an ancient being!')

    while True:
        user_choice = input(f'Care for another calculation?\n> ').lower()

        if user_choice == 'yes':
            print(f'That\'s the spirit!\nHere we go again...')
            return True

        elif user_choice == 'no':
            print('Ah fair enough, I guess I understand.\nSee you soon, I hope!')
            sys.exit()

        else:
            print('Remember, a simple yes or no is required here, my good friend.\n\nSo...', end='')
            continue


# --- PROGRAM EXECUTION AND LOOP ---

# Welcome Message
print("""
Welcome to my Division calculator!
It is a calculator which can only use division!
Not only that, but you can only input integers.
""")

if run_calculator_question_1():
    # Outer Loop: Allows for repeated calculations until the user quits.
    while True:

        # STEP 1: Execution waits here until the function returns True (valid input).
        calculator_input_validation()

        # STEP 2: The calculation is attempted. It returns True on success, False on failure.
        if division_calculation():

            # STEP 3: Only if the calculation was a success, ask to continue.
            run_calculator_question_2()


# End of Chapter 5 - Debugging Practice
