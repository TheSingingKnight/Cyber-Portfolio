"""
Python Learning Journal: Chapter 6 - LISTS.
File: lists_manipulation.py

Focus: Using Python's built-in list structure to store data and implementing robust control flow
       to manage user interaction and data manipulation.

Demonstrates:
- Core CRUD Operations: Implementing Create (Append), Read (Access/Search), Update (Modify), and Delete (Removal by Index).
- List Indexing and Boundary Checks: Ensuring user input remains within the list's valid index range (0 to length - 1).
- Control Flow Logic: Using nested while True loops alongside break, continue, and function return values to control the menu and repetition.
- Input Validation: Safely converting user string input to integers using try/except blocks.
- Global Scope Management: Using the globals() dictionary to dynamically create new variables (list copies) in the main program scope.
- List Methods: Utilizing specific list functions like .index() and the del statement.
"""

import sys, logging, copy

# --- GLOBAL VARIABLES ---


cathaven_city_locations_list = ('London', 'Birmingham', 'York', 'Glasgow', 'Nottingham', 'Canterbury', 'Ripon')

cathaven_ripon_cat_list = ['Luna', 'Crookshanks', 'Dobby', 'Minerva', 'Neville', 'Hagrid', 'Ginny', 'Sirius', 'Bellatrix', 'Lumos', 'Draco', 'Nox']


# --- LOGGING SETUP ---

# Sets the logging format and level. All messages at DEBUG level and above will be displayed.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program execution.')

# To save logs to a file instead of the console, uncomment the line below:
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# To disable all logging (for final release of the code), uncomment the line below:
# logging.disable(logging.CRITICAL)



# --- FUNCTION DEFINITIONS ---


# - Listing function -

def list_ripon_cats():
    global cathaven_ripon_cat_list

    while True:
        user_input = input(f'Enter\n1 to list all cats here in our Ripon home.\n2 to view a select range of cats.\n3 to return to the main menu.\n4 to exit the application.\n> ')

        if user_input == '1':
            print(f'\n--- Full List of Cats in Ripon CatHaven ---')
            for i in range(len(cathaven_ripon_cat_list)):
                print(f'ID {i}: {cathaven_ripon_cat_list[i]}')
            print('--------------------------------------------\n')
            continue # After printing, return to the function's menu loop.

        elif user_input == '2':
            # This section needs Try/Except for input validation (we'll fix this later)
            while True:
                first_id_input_str = input(f'Enter the starting ID from which you want to search from.\n> ')
                second_id_input_str = input(f'Enter the last ID from which you want to search up to.\n> ')

                # C. Fix: List slicing uses brackets and the colon [start:end]
                try:
                    start = int(first_id_input_str)
                    end = int(second_id_input_str)
                    print(f'\n--- Selected Range of Cats ---')
                    print(cathaven_ripon_cat_list[start:end])
                    print('------------------------------\n')
                except (ValueError, IndexError):
                    print(f'Invalid ID entered. Please use only numbers, and ensure they are within the range 0 to {len(cathaven_ripon_cat_list)}.')
                    continue # Re-ask for IDs
                break # Exit inner ID loop

            continue # Return to outer menu loop

        elif user_input == '3':
            return True # Returns to Main Menu

        elif user_input == '4':
            print(f'Thank you for visiting, we hope to see you soon!')
            sys.exit()

        else:
            print(f'You must enter a number from the options to continue.')
            continue



# - ID search function -

def idsearch_ripon_cats():
    global cathaven_ripon_cat_list

    while True: # Loop 1: Input and Validation
        cat_number_str = input(f'Enter the cat\'s ID number to pull up their information.\n> ')

        try:
            cat_number = int(cat_number_str)

            # --- CRITICAL LIST BOUNDARY CHECK (New Chapter 6 Concept) ---
            # Checks if the number is within the valid index range [0] to [length - 1]
            if 0 <= cat_number < len(cathaven_ripon_cat_list):
                break # Valid ID found, exit Loop 1
            else:
                # Log the boundary error
                logging.warning(f'User entered ID {cat_number}, which is outside the valid range.')
                print(f'ID {cat_number} is not a valid index. Please try a number between 0 and {len(cathaven_ripon_cat_list) - 1}.')
                continue # Re-ask the ID question

        except ValueError:
            # Log the type error
            logging.warning('User entered non-numeric value for cat ID.')
            print(f'Please enter a number.')
            continue # Re-ask the ID question

    # Execution reaches here ONLY if a valid cat_number (integer) was found.
    # Output the result first:
    print(f'Cat found at ID {cat_number}: {cathaven_ripon_cat_list[cat_number]}')

    while True: # Loop 2: Ask to continue/quit

        user_input = input(f'Enter\n1 to search another cat by ID number.\n2 to return to the main menu.\n3 to exit the application.\n> ')

        if user_input == '1':
            # Option 1: Search another cat. We exit the function and tell the main menu to call it again.
            return False # Signal to the main menu to call this function again

        elif user_input == '2':
            # Option 2: Return to the main menu.
            return True # Signal to the main menu to proceed to the main menu logic

        elif user_input == '3':
            print(f'Thank you for visiting, we hope to see you soon!')
            sys.exit()

        else:
            continue # Re-ask the Loop 2 menu question




# - Name search function -


def namesearch_ripon_cats():
    """Searches the list by name and returns the cat's ID."""
    global cathaven_ripon_cat_list

    while True: # Loop 1: Name Input and Search
        cat_name_str = input(f'Please enter the cat name you would like to search.\n> ').strip() # Added .strip() for clean input
        #The .strip() method removes any leading (at the beginning) and trailing (at the end) whitespace characters from a string.

        # A. Corrected Check: checks if the string exists in the list
        if cat_name_str in cathaven_ripon_cat_list:

            # Get the index (ID) of the cat
            cat_id = cathaven_ripon_cat_list.index(cat_name_str)

            print(f'\nWe do have a cat called {cat_name_str}.')
            print(f'The little one\'s ID is {cat_id}.\n')
            break # Exit Loop 1 after successful search

        else:
            print(f'I\'m sorry, we don\'t have a cat named {cat_name_str} here.\n')
            break # Exit Loop 1 after unsuccessful search (we ask the user what to do next in Loop 2)

    while True: # Loop 2: Menu after Search
        user_input = input(f'Enter\n1 to search another cat by name.\n2 to return to the main menu.\n3 to exit the application.\n> ')

        # Use string comparison and return False to repeat the function
        if user_input == '1':
            return False # Signal to Main Menu to repeat namesearch_ripon_cats()

        elif user_input == '2':
            return True # Signal to Main Menu to proceed to the main menu options

        elif user_input == '3':
            print(f'Thank you for visiting, we hope to see you soon!')
            sys.exit()

        else:
            print(f'Invalid option. Please try again.')
            continue # Restarts Loop 2 menu question


# - Delete function -

def delete_ripon_cat():
    """Removes a cat from the list by ID (index)."""
    global cathaven_ripon_cat_list

    while True: # Loop 1: ID Input and Outer Process Control
        remove_cat_str = input(f'Please enter the ID of the cat you wish to remove from our list.\n> ').strip()

        try:
            remove_id = int(remove_cat_str)

            # 1. Check if ID is valid
            if 0 <= remove_id < len(cathaven_ripon_cat_list):

                cat_name_to_remove = cathaven_ripon_cat_list[remove_id]
                print(f'\nThe cat with ID {remove_id} is {cat_name_to_remove}.')

                # --- START OF NESTED LOOP (Loop 1A: Confirmation Prompt) ---
                while True:
                    confirm_remove = input(f'Are you sure you want to remove {cat_name_to_remove}?\nPress 1 to confirm or 2 to abort.\n> ').strip()

                    if confirm_remove == '1':
                        del cathaven_ripon_cat_list[remove_id]
                        logging.info(f'Cat ID {remove_id} ({cat_name_to_remove}) successfully removed.')
                        print(f'ID {remove_id} - {cat_name_to_remove} has been successfully removed from our list.\n')
                        break # Exits the NESTED Loop 1A (Confirmation)

                    elif confirm_remove == '2':
                        # Deletion aborted
                        print(f'Removal aborted.\n')
                        break # Exits the NESTED Loop 1A (Confirmation)

                    else:
                        # Invalid confirmation input
                        print(f'You must enter 1 or 2 to continue.')
                        continue # Restarts the NESTED Loop 1A (Re-asks confirmation)
                # --- END OF NESTED LOOP (Loop 1A) ---
                break # Exits the OUTER Loop 1 (ID Input) and proceeds to Loop 2 (Menu)

            else:
                # Handle Index/Boundary Error
                print(f'We do not have a cat with ID {remove_id}. Valid IDs are 0 to {len(cathaven_ripon_cat_list) - 1}.\n')
                break # Exits the OUTER Loop 1 and proceeds to Loop 2 (Menu)

        except ValueError:
            logging.warning('User entered non-integer value for cat ID during deletion.')
            print(f'Invalid input. Please enter a number for the ID.\n')
            continue # Restarts the OUTER Loop 1 (Re-asks for ID)


    while True: # Loop 2: Menu after Deletion Attempt
        user_input = input(f'Enter\n1 to remove another cat from the list.\n2 to return to the main menu.\n3 to exit the application.\n> ').strip()

        if user_input == '1':
            return False

        elif user_input == '2':
            return True

        elif user_input == '3':
            print(f'Thank you for visiting, we hope to see you soon!')
            sys.exit()

        else:
            print(f'Invalid option. Please try again.')
            continue # Restarts Loop 2 menu question


# - Modify function -

def modify_ripon_list():
    """Modifies a cat's name in the list by ID (index)."""
    global cathaven_ripon_cat_list

    while True: # Loop 1: ID Input and Outer Process Control
        modify_cat_str = input(f'Please enter the ID of the cat you wish to modify from our list.\n> ').strip()

        try:
            modify_id = int(modify_cat_str)

            # ID must be strictly less than list length.
            if 0 <= modify_id < len(cathaven_ripon_cat_list):

                cat_name_to_modify = cathaven_ripon_cat_list[modify_id]
                print(f'\nThe cat with ID {modify_id} is currently named {cat_name_to_modify}.')

                # --- START OF NESTED LOOP (Loop 1A: Confirmation Prompt) ---
                while True:
                    confirm_modify = input(f'Are you sure you want to modify this record?\nPress 1 to confirm or 2 to abort.\n> ').strip()

                    if confirm_modify == '1':
                        modified_record = input(f'Please enter the new name for the cat.\n> ').strip()

                        cathaven_ripon_cat_list[modify_id] = modified_record

                        logging.info(f'Cat ID {modify_id} successfully changed from {cat_name_to_modify} to {modified_record}.')
                        print(f'\nID {modify_id} - has been successfully changed to {modified_record}.\n')
                        break

                    elif confirm_modify == '2':
                        print(f'Modification aborted.\n')
                        break

                    else:
                        print(f'You must enter 1 or 2 to continue.')
                        continue

                # --- END OF NESTED LOOP (Loop 1A) ---
                break # Exits the OUTER Loop 1 (ID Input) and proceeds to Loop 2 (Menu)

            else:
                # Invalid ID entered
                print(f'We do not have a cat with ID {modify_id}. Valid IDs are 0 to {len(cathaven_ripon_cat_list) - 1}.\n')
                break # Exits the OUTER Loop 1 and proceeds to Loop 2 (Menu)

        except ValueError:
            logging.warning('User entered non-integer value for cat ID during modification.')
            print(f'Invalid input. Please enter a number for the ID.\n')
            continue # Restarts the OUTER Loop 1 (Re-asks for ID)


    while True: # Loop 2: Menu after Modification Attempt
        user_input = input(f'Enter\n1 to modify another record from the list.\n2 to return to the main menu.\n3 to exit the application.\n> ').strip()

        if user_input == '1':
            return False

        elif user_input == '2':
            return True

        elif user_input == '3':
            print(f'Thank you for visiting, we hope to see you soon!')
            sys.exit()

        else:
            print(f'Invalid option. Please try again.')
            continue


# - Copy function -

def copy_ripon_list():
    """Demonstrates list copying using the copy module (Two-Loop Structure)."""
    global cathaven_ripon_cat_list

    while True: # Loop 1: Get Name and Attempt Copy
        copy_name_str = input(f'Please enter the file name for the copied version of our cat list, or leave blank to abort.\n> ').strip()

        if copy_name_str == '':
            print(f'List copy aborted.\n')
            break

        else:
            # We use globals() to save the new list under the user-defined variable name.
            globals()[copy_name_str] = copy.copy(cathaven_ripon_cat_list)

            print(f'\nSUCCESS: A copy of the list has been created and saved globally under the variable name: "{copy_name_str}"')
            print(f'The new list variable now contains: {globals()[copy_name_str]}\n')

            break

    while True: # Loop 2: Menu after Copy Attempt (Decide to repeat Loop 1 or exit)
        # Note: I changed the prompt to be clearer for the user.
        user_input = input(f'Enter:\n1 to make another copy.\n2 to return to the main menu.\n3 to exit the application.\n> ').strip()

        if user_input == '1':
            # Signal to Main Menu to repeat copy_ripon_list()
            return False

        elif user_input == '2':
            # Signal to Main Menu to proceed to the main menu options
            return True

        elif user_input == '3':
            print(f'Thank you for visiting, we hope to see you soon!')
            sys.exit()

        else:
            print(f'Invalid option. Please try again.')
            continue # Restarts Loop 2 menu question


# - Main menu -

def main_menu():
    print("""
    Welcome to CatHaven in Ripon.
    Here we look after lots of little ones, all hoping to find their forever home with a special family.
    """)

    while True: # Main menu loop - this runs until sys.exit() is called

        user_input = input("""
        Please input one of the following numbers.
        1 To see a list of the cats here.
        2 To search for a cat by ID.
        3 To search for a cat by name.
        4 To delete a cat from our records.
        5 To modify a cat from our records.
        6 To copy our records to a new file.
        7 To exit the application.
        > """).strip() # Added .strip() for clean input

        # --- Option 1: List Cats ---
        if user_input == '1':
            # This function returns True automatically, so no special check needed.
            list_ripon_cats()

        # --- Option 2: Search by ID ---
        elif user_input == '2':
            # Use an inner loop to force repetition if the function returns False
            while True:
                result = idsearch_ripon_cats()
                if result == True:
                    break # Exit inner while loop, return to outer main menu loop
                # If result is False, the loop naturally continues, calling the function again

        # --- Option 3: Search by Name ---
        elif user_input == '3':
            # Apply the same repetition logic
            while True:
                result = namesearch_ripon_cats()
                if result == True:
                    break

        # --- Option 4: Delete Cat ---
        elif user_input == '4':
            while True:
                result = delete_ripon_cat()
                if result == True:
                    break

        # --- Option 5: Modify Cat ---
        elif user_input == '5':
            while True:
                result = modify_ripon_list()
                if result == True:
                    break

        # --- Option 6: Copy Records ---
        elif user_input == '6':
            while True:
                result = copy_ripon_list()
                if result == True:
                    break

        # --- Option 7: Exit Application ---
        elif user_input == '7':
            print(f'Thank you for visiting, we hope to see you soon!')
            sys.exit()

        # --- Invalid Input ---
        else:
            print(f'Invalid option. Please try again.')
            continue


# --- START OF SCRIPT ---

main_menu()


# End of Chapter 6 - List Practice
