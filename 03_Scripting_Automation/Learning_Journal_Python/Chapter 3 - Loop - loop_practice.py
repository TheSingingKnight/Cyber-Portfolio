"""
Python Learning Journal: Chapter 3 - LOOPS.
File: loop_practice.py

Focus: Demonstrating the use of 'while True' loops, nested loops, 'break',
and 'sys.exit()' for program control flow.

Demonstrates:
- While loops for continuous and conditional iteration.
- Nested loops for input validation.
- The 'global' keyword for variable scope management.
- Arithmetic assignment operator (+=) for score incrementation.
- Modular code structure using functions.
"""

import random, sys

# --- GLOBAL VARIABLES & CONSTANTS ---

# These variables keep track of the number of wins, losses, and ties.
# Note: These must be declared 'global' inside start_game_loop() if their values are changed.
wins = 0
losses = 0
ties = 0

# DEFINES the list of choices for the game logic.
# Use a tuple () instead of a list [] as the moves list should not change (immutable).
MOVES = ('rock', 'paper', 'scissors', 'lizard', 'spock')


# --- PRE-GAME SETUP FUNCTION ---
def pre_game_setup():
    """
    Handles the user's readiness check and prints the game rules.
    This function uses while loops to force valid user input before the game starts.
    """
    print('Welcome to the fan-favourite game Rock, Paper, Scissors, Lizard, Spock!')
    print('Here you will play against our resident champion of the game, Sheldon.')

    # LOOP 1: Initial readiness check (Loop forces a valid yes/no)
    while True:
        # Use \n for a clean newline space for visual spacing/clarity; .lower() ensures consistent checking.
        courage_test_1_input = input('\nDo you have what it takes to go toe to toe with this legend?\n> ').lower()

        if courage_test_1_input == 'yes':
            print('\nThat\'s the spirit!')
            break
        elif courage_test_1_input == 'no':
            print('\nThis is understandable, the (figuratively) towering figure of our resident Dr. has that effect on many.')
            break  # Break is necessary here to exit the 'while True' loop.
        else:
            # If the answer is not 'yes' or 'no', the loop repeats automatically.
            print('\nWhat is required here is a simple, yet resolute, yes or no.')


    # Print the rules using triple quotes for multi-line formatting (PEP 8 standard).
    print("""
Now, for those who don\'t know the rules to this iconic game, they are as follows...

Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock,
Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper,
Paper disproves Spock, Spock vaporizes Rock, and as it always has, Rock crushes Scissors.

If that\'s a lot to take in, simply remember the order of ...

**Rock, Spock, Paper, Lizard, Scissors.** Each one beats the two before it and is beaten by the two after it.
""")

    # LOOP 2: Final confirmation check before starting the game
    while True:
        courage_test_2_input = input('Still think you can take on Captain Cooper?\n> ').lower()

        if courage_test_2_input == 'yes':
            print('\nExcellent! Let the battle commence!')
            # return True exits the function and passes a successful status back to the main program.
            return True
        elif courage_test_2_input == 'no':
            print('\nPerhaps another time. Farewell.')
            # sys.exit() is used for immediate, clean program termination when the user quits.
            sys.exit()
        else:
            print('\nBe true to yourself and singular in mind. Answer either yes or no.')



# --- MAIN GAME LOOP FUNCTION ---
def start_game_loop():
    """
    Contains the core game logic: player input, computer choice,
    win/loss determination, score tracking, and the main game loop.
    """
    # Declare variables as global so the function can modify the scores set outside the function's scope.
    global wins, losses, ties

    while True: # Main game loop: plays indefinitely until the user quits
        print('\n----------------------------------------')
        # Print current score (Looping demonstration for score keeping)
        print(f'W: {wins}, L: {losses}, T: {ties}')

        # Player Input Loop (NESTED LOOP: ensures the user enters a valid move or 'q' to quit)
        while True:
            print('\nEnter your move: (r)ock (p)aper (s)cissors (l)izard (k)spock or (q)uit')
            player_move = input('> ').lower()

            if player_move == 'q':
                # sys.exit() is used here to terminate the entire program from within the main loop.
                sys.exit()

            # Convert single-letter input to full move name
            if player_move.startswith('r'):
                player_move = 'rock'
                break
            elif player_move.startswith('p'):
                player_move = 'paper'
                break
            elif player_move.startswith('s'):
                player_move = 'scissors'
                break
            elif player_move.startswith('l'):
                player_move = 'lizard'
                break
            elif player_move.startswith('k'): # Using 'k' for Spock to avoid conflict with 's'
                player_move = 'spock'
                break
            else:
                print('Invalid move. Please choose r, p, s, l, k, or q.')

        # Computer's move (Using random.choice() from the imported 'random' module)
        computer_move = random.choice(MOVES)
        print(f'Sheldon chooses: {computer_move.upper()}!')

        # --- WIN/LOSS LOGIC (Complex Flow Control) ---

        # 1. TIE Condition
        if player_move == computer_move:
            print('It is a TIE!')
            # Use the += operator (shorthand for ties = ties + 1), which is the standard,
            # efficient, and Pythonic way to increment a variable's score.
            ties += 1

        # 2. WIN Condition (Uses complex Boolean logic for win patterns)
        # Note: Each move beats the two that follow it in the MOVES list sequence.
        elif (player_move == 'rock' and (computer_move == 'scissors' or computer_move == 'lizard')) or \
             (player_move == 'paper' and (computer_move == 'rock' or computer_move == 'spock')) or \
             (player_move == 'scissors' and (computer_move == 'paper' or computer_move == 'lizard')) or \
             (player_move == 'lizard' and (computer_move == 'spock' or computer_move == 'paper')) or \
             (player_move == 'spock' and (computer_move == 'scissors' or computer_move == 'rock')):

            print('YOU WIN! Bazinga!')
            # Use the += operator (shorthand for wins = wins + 1).
            wins += 1

        # 3. LOSS Condition (The 'catch-all' else)
        else:
            print('You lose. Sheldon reigns supreme!')
            # Use the += operator (shorthand for losses = losses + 1).
            losses += 1


# --- PROGRAM EXECUTION ---

# Call the setup function. If it returns True (user is ready), start the game loop.
if pre_game_setup():
    start_game_loop()

# End of Chapter 3 - Loop Practice
