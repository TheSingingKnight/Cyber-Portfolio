"""
Python Learning Journal: Chapter 9 - Text pattern matching with regular expressions.
File: regex_extractor.py

Focus: Using Python's 're' module to define, compile, and execute powerful text patterns
       for data extraction, validation, and sanitization (masking).

Demonstrates:
- Core Workflow: Import, re.compile(), re.findall(), and using Match Objects (mo).
- Advanced Compilation: Using the re.VERBOSE flag to make complex patterns readable with comments.
- Anchors: Using ^ (start-of-string) and $ (end-of-string) for full string validation.
- Character Classes: Using [a-zA-Z] and the negative class [^...] (e.g., [^\s] for no whitespace).
- Grouping & Quantifiers: Defining () groups, \d, \w, and specific quantifiers like {3,4}.
- Substitution: Utilizing the re.sub() method with back-references (\1) to mask sensitive data.
- Integration: Using the pyperclip module to process text directly from the system clipboard.
"""

import re, pyperclip


# ----------------------------------------------------------------------
# --- STATION 1: DATA EXTRACTION ---
# ----------------------------------------------------------------------

def Station_1():

    print("\n--- STATION 1: Phone number and Email data extraction ---")

    # --- Pattern 1: Standard European Phone Number (Showcases Groups, Quantifiers, Escaping, Pipes) ---
    phone_re = re.compile(r'''(
        (\+\d{1,4}|\d{2,4})?      # Optional Country/Local Code (e.g., +44 or 07)
        (\s|-|\.)?                # Separator 1
        (\d{3,4})                 # Block 1 (3 or 4 digits, e.g., area/mobile code)
        (\s|-|\.)?                # Separator 2
        (\d{3,4})                 # Block 2 (3 or 4 digits)
        (\s|-|\.)?                # Separator 3
        (\d{3,4})                 # Block 3 (3 or 4 digits)
    )''', re.VERBOSE)

    #In VERBOSE mode, Python tells the regex engine to ignore all whitespace and treat any text following a # symbol until the end of the line as a comment.

    # --- Pattern 2: Email Address (Showcases Character Classes) ---
    email_re = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # Username (Allows letters, numbers, dot, underscore, percent, plus, and literal hyphen)
        @                       # The necessary @ symbol
        [a-zA-Z0-9._%+-]+       # Domain Name
        (\.[a-zA-Z]{2,4})       # Dot-Something (TLD, e.g., .com or .uk)
    )''', re.VERBOSE)


    # --- Finding Matches (Demonstrates re.findall and Group Access) ---
    matches = []
    text = pyperclip.paste() # Get text from the clipboard

    # Adding the found phone numbers to the matches list.
    for groups in phone_re.findall(text):
        # groups[0] is the entire match. groups[1] is Country Code, [3] is Block 1, etc.
        phone_num = ' '.join([groups[1], groups[3], groups[5], groups[7]])
        matches.append(phone_num)

    # Adding the found emails to the matches list.
    for groups in email_re.findall(text):
        matches.append(groups[0]) # groups[0] contains the entire email match.


    # --- Copying results to the clipboard ---
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')



# ----------------------------------------------------------------------
# --- STATION 2: ADVANCED VALIDATION AND FORMATTING ---
# ----------------------------------------------------------------------

def Station_2():

    print("\n--- STATION 2: Advanced Validation and Formatting ---")
    print("Goal: Validate a 'Stardate ID' using Anchors and Negative Character Classes.")

    # --- Pattern: Stardate ID Validator ---
    # Goal: Must start with a letter, be 8 characters long, and contain NO spaces.

    # Pattern Breakdown:
    # 1. ^[A-Za-z] : Must START (^) with one letter.
    # 2. [^\s]{7} : Must contain 7 of ANY character that is NOT (^) a whitespace (\s).
    # 3. $ : Must end ($) immediately after the last character.
    stardate_id_re = re.compile(r'^[A-Za-z][^\s]{7}$', re.I) # re.I is Ignore Case

    print("-" * 50)

    while True:
        id_input = input("Enter an 8-character Stardate ID (must start with a letter, no spaces).\n> ")

        # Use the .search() method to see if the entire string matches the anchored pattern.
        mo = stardate_id_re.search(id_input)
        # mo is an extremely common, idiomatic convention in the Python community when working with the re module.
        # mo is simply an abbreviation for "Match Object."


        # Note: We cannot use 'if len(mo) > 0:' to check for a match.
        # This is because mo (the Match Object) is not a list, string, or any other data type.
        # When Python finds a match, mo is an object. When it fails to find a match, mo is assigned the special value None.
        if mo is not None:
            print(f"VALIDATION SUCCESS: '{id_input}' is a valid 8-character Stardate ID.")
            break
        else:
            print("VALIDATION FAILED. Remember: must be 8 chars, start with a letter, and contain no spaces.")
            # Note: The anchor system forces all three rules simultaneously.
            # This is esentially a neater/optimised way of validation.




# ----------------------------------------------------------------------
# --- STATION 3: DATA PMASKING AND CLEANING ---
# ----------------------------------------------------------------------

def Station_3():

    print("\n--- STATION 3: Data Masking and Cleaning ---")

    # Text to be censored
    raw_text = pyperclip.paste()
    print(f"Original Text (from clipboard):\n{raw_text[:80]}...") # Showing a snippet!

    # --- Pattern 1: Star Command ID Recognizer (Masking Showcase) ---
    # Goal: Find the 3-2-4 pattern (with optional rank) for replacement.
    id_mask_re = re.compile(r'''(
        (\d{3})                 # Group 1: First three digits (KEPT UNMASKED)
        -?                      # Optional hyphen (NOT grouped)
        \d{2}                   # Two digits (MASKED)
        -?                      # Optional hyphen
        \d{4}                   # Four digits (MASKED)
        (-?\d{1,2})?            # Optional Rank (Group 2: Entirely MASKED)
    )''', re.VERBOSE)

    # --- Substitution/Masking Star Command ID (Demonstrates re.sub) ---
    # The substitution string uses:
    # \1: Back-reference to Group 1 (the first 3 digits) - KEPT
    # -XX-XXXX: Literal replacement for the rest of the sensitive digits. - MASKED

    censored_text = id_mask_re.sub(r'\1-XX-XXXX', raw_text)

    print("-" * 50)
    print("Masking with .sub():")
    print(f"Censored Version: {censored_text}")


    # Optional: Copy the censored text back to the clipboard
    pyperclip.copy(censored_text)
    print("\nCensored text copied back to clipboard.")


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
    print("\n--- Script finished. All Chapter 9 concepts showcased. ---")


# End of Chapter 9 - Text pattern matching with regular expressions.


