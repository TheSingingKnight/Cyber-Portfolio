"""
Python Learning Journal: Chapter 10 - Reading and Writing Files.
File: file_io.py

Focus: Mastering modern file handling using the 'pathlib' module for path management
       and demonstrating various methods for reading, writing, and persisting data
       using text files and the 'shelve' module.

Demonstrates:
- Pathlib Convention: Importing 'Path' directly for modern file system interaction.
- Path Inspection: Using .parent, .name, .stem, .suffix, .parts, and .parents to analyze path structure.
- Navigation: Utilizing os.chdir() and Path.cwd() to simulate directory traversal.
- File Discovery: Using Path.glob() with wildcards to find files (e.g., '*.txt').
- Read/Write: Using the concise .read_text() and .write_text() methods.
- Safety: Using the 'with open(..., 'a', encoding='UTF-8')' convention for safe file appending.
- Caution: Highlighting the destructive nature of write mode ('w').
- Data Persistence: Saving Python objects (lists) to a binary file using the 'shelve' module.
"""


import os, random
from pathlib import Path

# It is convention to import Path like this because:
# It avoids writing 'pathlib.Path' every time you use it.


# ----------------------------------------------------------------------
# --- STATION 1: PATH MANAGEMENT AND METADATA ---
# ----------------------------------------------------------------------

def Station_1():

    print("\n" + f'Montressor Spaceport: AdHoc Security Station'.center(60, '='))

    # Simulated Change (os.chdir and Path.cwd())
    # Note: This is simulated. You need to ensure the path exists on your system or comment it out.
    print(f'Attempting to navigate to Security Command Directory...')

    try:
        os.chdir(r'C:\Montressor\Security_Logs')
    except FileNotFoundError:
        # Fallback for systems where the path doesn't exist
        print("Note: Cannot change directory. Using current directory as base.")
        pass
        #pass eyword in a try/except block is a placeholder that tells Python to do absolutely nothing when a specific error occurs.

    print(f'New working directory (Path.cwd()):\n{Path.cwd()}')
    print("-" * 60)

    # Path Properties (.parent, .name, .stem, .suffix)
    # Creating a sample log file path to inspect (using the / operator to join parts)
    log_file = Path.cwd() / 'MS-LOG-1092_2025.txt'

    print(f'Inspecting Path Properties of a simulated file: {log_file.name}')
    print(f'''
    Parent Directory = {log_file.parent}
    File Name        = {log_file.name}
    File Stem (Base) = {log_file.stem}
    File Suffix (Ext)= {log_file.suffix}
    Drive (if present) = {log_file.drive}
    ''')
    print("-" * 60)


    # Advanced Properties (.parts and .parents)
    print(f'Breaking file path down into parts for easier viewing (Path.parts):')

    log_parts = log_file.parts
    print(log_parts)

    # Using enumerate to correctly display the index and the part.
    print(f'\nDetailed Breakdown:')
    for index, part in enumerate(log_parts):
        print(f'Part {index}: {part}')

    print(f'\nParent Traversal (Path.parents):\n{list(log_file.parents)}')
    print("-" * 60)


    # File Existence & Glob
    # NOTE: This only works if you create a test file in the directory!

    # Checking for the existence of the specific file
    print(f'Checking for existence of the log file: {log_file.name} -> {log_file.exists()}')

    # Finding files using glob
    # Simulates finding all log files (*.txt)
    print(f'\nScanning directory for all *.txt files (Path.glob):')

    # Note: .glob() returns a generator; we use a list comprehension to print it neatly.
    log_files_found = [p.name for p in Path.cwd().glob('*.txt')]

    if log_files_found:
        print(f"Found {len(log_files_found)} files: {log_files_found}")
    else:
        print("No *.txt files found to list.")



# ----------------------------------------------------------------------
# --- STATION 2: CONTENT I/O AND SHELVING ---
# ----------------------------------------------------------------------

def Station_2():

    print("\n" + f'Montressor Spaceport: Log Analysis'.center(60, '='))

    # 2. Log Simulation (Creating the actual files)
    print(f'Creating placeholder logs for security testing...')

    # We define a list of log paths and create them using .write_text('')
    log_paths = [Path.cwd() / f'MS-LOG-109{i}_2025.txt' for i in range(2, 8)] # Creates MS-LOG-1092 to MS-LOG-1097

    # Use write_text('') to create the files on the system (or ensure they exist)
    for p in log_paths:
        p.write_text('Log body entry placeholder.')

    # A simulation list of "critical" events (not file names)
    critical_event_list = [
        "Unauthorized Hull Scan (Sector Beta)",
        "Suspicious Drone Activity (Cargo Bay 4)",
        "Life Support Fluctuation (Airlock 7)",
        "Unknown Signal Intercept (Deep Space Array)"
    ]

    print(f'Placeholder Logs created.')
    print("-" * 60)

    # 3. Content Sampling (random.sample)
    print(f'Sampling a random selection of critical events for immediate action...')

    # Sample 2 items from the critical event list
    random_action_events = random.sample(critical_event_list, 2)

    print(f'Selected for Review:\n- {random_action_events[0]}\n- {random_action_events[1]}')
    print("-" * 60)

    # 4. Destructive Write (.write_text)
    # Target path for the summary file
    summary_path = Path.cwd() / 'Critical_Logs_Summary.txt'

    print(f'Generating new summary file: {summary_path.name}')

    # Convert the list to a single string with line breaks before writing
    content_to_write = '\n'.join(critical_event_list)

    summary_path.write_text(content_to_write, encoding='UTF-8')

    # CAUTIONARY NOTE:
    print("NOTE: Using .write_text() in this step completely OVERWROTE the previous file content.")
    print("-" * 60)

    # 5. Reading Content (.read_text)
    print(f'Verifying content of the new summary file:')

    # Use read_text to quickly grab and display the content
    file_content = summary_path.read_text(encoding='UTF-8')
    print(file_content)
    print("-" * 60)


    # 6. Safe Append (with open)
    # This demonstrates the safest way to append content.
    print(f"Opening file in append mode to log confirmation signature.")

    # The 'a' mode opens in append. 'as f' assigns the file object to 'f'.
    with open(summary_path, 'a', encoding='UTF-8') as f:
        f.write("\n\n--- CONFIRMED by MS Security Officer (APPEND MODE) ---")

    print("Confirmation appended using 'with open(..., 'a', encoding='UTF-8')'.")
    print("-" * 60)

    # 7. Shelving Data (Saving Python objects)
    print(f"Shelving the complete list of critical events for permanent storage...")

    # Open the shelve file (creates 'data.dat' and related files)
    # The 'with' statement ensures the shelve file is always closed and saved.
    with shelve.open('critical_data') as db:
        db['critical_events'] = critical_event_list # Save the list to the key 'critical_events'
        db['last_update'] = "2025-11-10"

    print("Critical event list saved to 'critical_data.dat' using the shelve module.")

    # Clean up the placeholder files created earlier
    for p in log_paths:
        if p.exists():
            p.unlink()


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

    print("\n--- Script finished. All Chapter 10 concepts showcased. ---")


# End of Chapter 10 - Reading and Writing Files.

