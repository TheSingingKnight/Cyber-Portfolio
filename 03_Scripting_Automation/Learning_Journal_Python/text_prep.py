"""
Python Learning Journal: Chapter 8 - Strings and Text Editing.
File: text_prep.py

Focus: Using simple text editing commands to help sanitise and format user input
       and script output.

Demonstrates:
- String Syntax: Raw Strings (r'...') to handle escape sequences literally.
- Indexing & Slicing: Accessing parts of a string using positive and negative indices.
- Validation Methods: Using .isalpha() and .isdecimal() to check content integrity.
- Advanced Cleaning: Utilizing .strip() to remove specific leading/trailing characters (not just whitespace).
- Parsing & Rebuilding: Efficiently converting between string and list using .split() and .join().
- Output Formatting: Creating columnar output using .ljust() and .rjust().
"""

# ----------------------------------------------------------------------
# --- STATION 1: RAW STRINGS AND INDEXING SHOWCASE ---
# ----------------------------------------------------------------------

def Station_1():

    print("\n--- STATION 1: Raw Strings and Indexing ---")

    # 1a. Raw String Syntax (r'...')
    # A raw string treats backslashes (\) literally, essential for file paths or regex patterns.
    # Preventing them from being interpreted as escape sequences (\t, \n).
    raw_path_string = r'C:\Users\CaptainAmelia\StarCharts\Legacy_Manifests\Treasure_Map_Coords.dat'
    print(f"File Path (Raw String): {raw_path_string}")
    print("-" * 40)

    # 1b. Positive Indexing and Slicing
    # Extracts the username segment 'CaptainAmelia' by counting from the start.
    username_segment = raw_path_string[10:23]
    print(f"Segment [10:23] (Username): {username_segment}")

    # 1c. Negative Indexing and Slicing
    # Extracts the file extension (.dat)
    file_extension = raw_path_string[-4:]
    print(f"Last 4 chars (Extension): {file_extension}")

# ----------------------------------------------------------------------
# --- STATION 2: TEXT VALIDATION AND CLEANING ---
# ----------------------------------------------------------------------

def Station_2():

    print("\n--- STATION 2: Text Validation and Cleaning ---")
    print("Welcome Spacefarer! Please create an account at the Montressor Spaceport.")

    # 2a. Validation Showcase (.isalpha() and .isdecimal())
    while True:

        username_input = input("Please enter a username (letters only).\n> ").strip()

        if username_input.isalpha() and len(username_input) > 0:

            pin_input = input("Please enter a PIN (numbers only).\n> ").strip()

            if pin_input.isdecimal() and len(pin_input) == 4:
                print(f"Thank you, {username_input}. Account PIN verified.")
                break
            else:
                print(f"PIN must be exactly 4 digits and contain only numbers.")

        else:
            print(f'Username must contain only letters and cannot be empty.')

    # 2b. Advanced .strip() Showcase
    # Demonstrates removing specific non-whitespace characters (., and !)
    raw_input = input("\nEnter a message (include some punctuation at the ends).\n> ")
    clean_input = raw_input.strip('.,! ') # Removes periods, commas, exclamations, and whitespace
    print(f"Original Input: '{raw_input}'")
    print(f"Cleaned Input (strip '.,! '): '{clean_input}'")


# ----------------------------------------------------------------------
# --- STATION 3: DATA PARSING AND RECONSTRUCTION ---
# ----------------------------------------------------------------------

def Station_3():

    print("\n--- STATION 3: Data Parsing and Reconstruction ---")

    # 3a. .split() Showcase
    # Breaks the single input string into a list of separate names.
    user_input = input("Please enter the names of your individual crew members, separating each with a comma.\n> ").strip().lower()

    # .split(',') breaks the string at every comma, creating a list of names.
    # Note: This often leaves leading whitespace on subsequent items.
    user_input_list = user_input.split(',')

    print(f"List of names created by .split(','): {user_input_list}")

    # 3b. .join() Showcase (Using List Comprehension for Pre-Formatting)

    # Step 1: List Comprehension (pre-formatting each item)
    # This runs through the list and pre-formats every name by:
    # 1. Calling .strip() to remove any extra spaces from the .split() step.
    # 2. Calling .title() to capitalize the name.
    # 3. Using an f-string to add the prefix "Crewman " to the start of every name.
    formatted_names = [f"Crewman {name.strip().title()}" for name in user_input_list]

    # Step 2: .join()
    # Joins the fully formatted names back into a single string using a single comma and space (", ")
    # as the separator *between* items. This avoids adding trailing punctuation!
    final_output = ", ".join(formatted_names)

    print(f"Reconstructed String (.join): {final_output}")

    # 3c. .ljust() and .rjust() Showcase (Columnar Formatting)
    # Creates clean, column-aligned output.
    print("\n--- Columnar Formatting (.ljust/.rjust) ---")
    header_1 = "SYSTEM STATUS"
    header_2 = "ACCESS LEVEL"

    # .ljust(30): left-justifies, padding with spaces up to 30 chars.
    # .center(15, '='): centers, padding with '=' up to 15 chars.
    print(header_1.ljust(30) + header_2.center(15, '='))
    print(f"Active User".ljust(30) + "Alpha".center(15))
    print(f"Secure Connection".ljust(30) + "Beta".center(15))


# ----------------------------------------------------------------------
# --- MAIN EXECUTION ---
# ----------------------------------------------------------------------

# 1. SPECIAL VARIABLE: Python automatically defines the variable __name__ for every script.
#    - If you run the file directly (e.g., 'python text_prep.py'), Python sets __name__ to "__main__".
#    - If another script imports this file (e.g., 'import text_prep'), Python sets __name__ to "text_prep".

if __name__ == "__main__":
    # 2. GOOD PRACTICE: This conditional block ensures that the function calls inside it
    #    will ONLY execute when the script is run directly by the user, not when it is
    #    imported as a module by another program.
    Station_1()
    Station_2()
    Station_3()
    print("\n--- Script finished. All Chapter 8 concepts showcased. ---")


# End of Chapter 8 - Strings and text editing.
