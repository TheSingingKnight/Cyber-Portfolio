"""
Python Learning Journal: Chapter 4 - FUNCTIONS.
File: collatz.py

Focus: Demonstrating function definition, parameter passing, return values,
       and robust error handling.

Demonstrates:
- Call Stack: Functions calling other functions (main -> input check -> collatz).
- While loops for continuous and conditional iteration.
- try/except block for graceful error handling (ValueError).
- The 'global' keyword for variable scope management.
- Optional print parameters (end) for custom output formatting.
- for i in range() for controlled iteration.
"""

# --- GLOBAL VARIABLES ---
# This variable tracks the total steps taken across all sequences in a session.
TOTAL_STEPS_CALCULATED = 0


# --- CORE CALCULATION FUNCTION ---
def collatz_sequence(number):
    """Calculates and prints the Collatz sequence for a given positive integer."""
    global TOTAL_STEPS_CALCULATED # Declare access to the global variable
    steps = 0

    # Print the introductory text using end=' ' to keep it on the same line as the sequence
    print(f"Sequence for {number}: ", end='')

    while number != 1:
        # We print the current number *before* calculating the next one
        print(number, end=' -> ')

        if (number % 2) == 0:
            # Even: Divide by 2
            number = number // 2
        else:
            # Odd: Multiply by 3 and add 1
            number = number * 3 + 1

        steps += 1
        TOTAL_STEPS_CALCULATED += 1 # Update the global variable on every step

    print(1) # Print the final '1' to terminate the sequence output cleanly
    print(f"(Finished in {steps} steps)")
    return steps # Return the number of steps
    # CRITICAL UNDERSTANDING: The function prints the sequence and finishes.
    # It returns a single INTEGER (the step count), which is saved in steps_taken.


# --- INPUT AND VALIDATION FUNCTION ---
def get_user_number():
    """Loops until the user enters a valid positive integer, handling errors."""
    while True:
        user_input = input('Care to give it a whirl?\n Enter a positive integer here...\n> ')

        try:
            val = int(user_input)

            if val <= 0:
                print("Sorry, input must be a positive integer, try again.")
                continue

            return val # Return the valid integer and break the loop

        except ValueError:
            # Graceful error handling using try/except
            print("Please enter a valid integer.")
            continue


# --- PROGRAM EXECUTION AND LOOP ---

# Welcome Message
print("""
Welcome to the Collatz Sequence Script!

The Collatz Sequence is a famous mathematical problem.

Starting with any positive number, the sequence does one of two calculations.
Depending whether the number is even or odd.

If even, the number is divided by 2.
If odd, the number is timesed by 3 with 1 added at the end.

This repeats until the final number reaches 1.

Amazingly enough, this sequence actually works for any integer; sooner or later, you’ll arrive at 1.
Even mathematicians aren’t sure why!

With this script you can test out any number and see the process play out.
""")

# Main loop to allow the user to run multiple sequences
while True:
    # 1. Call Stack: Calls the input validation function
    start_number = get_user_number()

    # 2. Main Action: Run the Collatz Sequence
    # CRITICAL UNDERSTANDING: The function prints the sequence and finishes.
    # It returns a single INTEGER (the step count), which is saved in steps_taken.
    steps_taken = collatz_sequence(start_number)

    # 3. for i in range() Demonstration: Visual representation of the number of steps taken.
    print("\n-- Incredibly exciting visual representation of steps in * ! --")

    for i in range(steps_taken):
        # Optional Parameter (end) used here to print all markers on one line
        print(' * ', end='')

    print(f"\n\nTotal steps calculated this session: {TOTAL_STEPS_CALCULATED}")


    # 4. Ask if the user wants to run another sequence
    if input("\nRun another sequence, ye old math addict? (yes/no): ").lower().startswith('n'):
        print("Thank you for using the Collatz Sequence Script. Ciao!")
        sys.exit() # Exit the program
