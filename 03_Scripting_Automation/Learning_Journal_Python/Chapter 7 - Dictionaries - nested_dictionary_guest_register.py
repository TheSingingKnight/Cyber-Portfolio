"""
Python Learning Journal: Chapter 7 - NESTED DICTIONARIES AND ROBUST DATA MANAGEMENT.
File: tavern_guest_system.py

Focus: Using nested dictionaries to structure complex data (guest files) and implementing
        robust methods for data reading and manipulation.

Demonstrates:
- Nested Dictionary Structure: Accessing and modifying values with sequential bracket notation ([][]).
- Robust Data Access: Utilizing .get() and .setdefault() methods to prevent KeyErrors
  when reading optional or potentially missing nested keys.
- Data Consistency: Applying formatting rules only to generic descriptive data (ranks, rooms)
  while preserving the exact case for proper nouns (ship names).
- Nested Value Updates: Simultaneously modifying multiple nested integer values (e.g., debt
  and meal counter) using the compound assignment operators (+=, -=).
- Code Reuse: Implementing efficient programming practice by calling retrieval functions
  to confirm modifications.
"""

# --- GLOBAL VARIABLES ---

tavern_guests = {
    'jim_hawkins':        {'rank': 'cabin boy', 'credits_owed': 175, 'meals_consumed': 3, 'room_type': 'transient_hammock', 'docked_ship': 'RLS Legacy'},
    'captain_amelia':     {'rank': 'ship captain', 'credits_owed': 440, 'meals_consumed': 3, 'room_type': 'captain_quarters', 'docked_ship': 'RLS Legacy'},
    'morph':              {'rank': 'companion pet', 'credits_owed': 0, 'meals_consumed': 7, 'docked_ship': 'RLS Legacy'},
    'mr_arrow':           {'rank': 'first mate', 'credits_owed': 360, 'meals_consumed': 3, 'room_type': 'standard_bunk', 'docked_ship': 'RLS Legacy'},
    'long_john_silver':   {'rank': 'cook', 'credits_owed': 295, 'meals_consumed': 4, 'docked_ship': 'RLS Legacy'},
    'dr_delbert_doppler': {'rank': 'astronomer', 'credits_owed': 720, 'meals_consumed': 6, 'room_type': 'premium_bunk'},
    'delilah':            {'rank': 'beast_of_burden', 'credits_owed': 0, 'meals_consumed': 4, 'room_type': 'stables'}
}


# --- FUNCTION DEFINITIONS ---


# -- List Guests --
def list_all_guests(guests):
    """
    Prints a formatted, tabulated list of all current tavern guests and their ranks.
    This demonstrates safe data access and clean string formatting.
    """

    print("\n--- Current Guests at The Starboard Tankard ---")

    # 1. GUARANTEE KEY EXISTENCE (Best Practice)
    # This loop ensures that the 'rank' key exists for every guest, setting it to 'Unknown'
    for guest_data in guests.values():
        guest_data.setdefault('rank', 'unknown')

    print("-" * 55)
    print(f"| {'NAME':<20} | {'RANK':<30} |") # Print the header row
    print("-" * 55)

    # 2. ITERATE AND UNPACK
    # We use .items() to get both the key (name) and the value (guest_data) for the loop.
    for name, data in guests.items():

        # 3. DIRECT BRACKET ACCESS (Safely guaranteed by setdefault above)
        # We can use data['rank'] instead of data.get('rank', 'unknown') because
        # setdefault() guarantees the key exists, which is slightly faster.
        raw_rank = data['rank']

        # 4. FORMATTING
        # Format the rank: Converts 'cabin boy' to 'Cabin Boy'
        formatted_rank = raw_rank.replace('_', ' ').title()
        # Format the name: Converts 'jim hawkins' to 'Jim Hawkins'
        formatted_name = name.replace('_', ' ').title()

        # 5. PRINT THE TABULAR RESULT (Uses f-string formatting specifiers)
        # Formatting Breakdown:
        # - :<20  -> Reserves 20 characters of width and left-aligns the name.
        # - :<30  -> Reserves 30 characters of width and left-aligns the rank.
        print(f"| {formatted_name:<20} | {formatted_rank:<30} |")

    print("-" * 55)


# -- Retrieve Guest File --
def retrieve_guest_file(guest):
    """
    Displays the file for a single guest, ensuring all necessary keys exist
    using setdefault(), and formats the output cleanly.
    """

    # 1. CHECK FOR GUEST EXISTENCE (Uses the 'in' operator)
    if guest in tavern_guests:

        # Access the specific guest's nested dictionary data directly
        guest_data = tavern_guests[guest]

        print("\n--- The Starboard Tankard Guest File ---")
        print(f"Name: {guest.replace('_', ' ').title()}")

        # 2. APPLY SETDEFAULT TO ENSURE ALL KEYS EXIST
        # This is good practice: it guarantees every file has these keys before we access them.
        # By supplying the default value ('transient_hammock' or 'stables') if the key is missing.
        guest_data.setdefault('rank', 'unknown')
        guest_data.setdefault('credits_owed', 0)
        guest_data.setdefault('meals_consumed', 0)
        guest_data.setdefault('room_type', 'transient_hammock')
        guest_data.setdefault('docked_ship', 'None')

        # 3. ITERATE AND PRINT THE NESTED DATA (Using Tuple Unpacking)
        for key, value in guest_data.items():

            # Formatting the Key: Converts 'credits_owed' to 'Credits Owed' for display.
            # We use .replace() to swap the underscore, then .title() to capitalize words.
            formatted_key = key.replace('_', ' ').title()

            # Formatting the Value: Requires a data type check (isinstance) for safety.
            if isinstance(value, str):
                # If the value is a string (e.g., 'ship captain'), format it cleanly.
                formatted_value = value.replace('_', ' ').title()
            else:
                # If the value is NOT a string (it's an integer like 720), leave it as-is.
                # This prevents a crash (e.g., you can't run 720.replace()).
                formatted_value = value

            # Final Print: Combines the formatted key and value.
            print(f"- {formatted_key}: {formatted_value}")

        print("-" * 30)


    else:
        # Error message if the initial 'in' check fails
        print(f"\nError: Guest '{guest.title()}' not found in The Starboard Tankard system.")



# -- Add New Guest --
def add_guest():
    """
    Starts an interactive process to add a new guest to the tavern_guests file,
    demonstrating direct dictionary assignment to create a new key and nested value.
    """
    global tavern_guests # Needed because we are ADDING to the global dictionary

    print("\n--- Registering New Guest at The Starboard Tankard ---")

    # --- 1. GATHERING AND CLEANING INPUT ---
    # We apply a chain of methods to ensure a clean snake_case string is produced:
    # 1. .strip() removes leading/trailing spaces (e.g., '  john  ' -> 'john')
    # 2. .lower() ensures everything is lowercase (e.g., 'John' -> 'john')
    # 3. .replace(' ', '_') replaces internal spaces with underscores (e.g., 'john silver' -> 'john_silver')

    name_input = input('Please enter the name of the new guest.\n> ').strip().lower()

    # Check if the guest already exists (using the key they just typed)
    if name_input.replace(' ', '_') in tavern_guests:
        print(f"\nError: Guest '{name_input.title()}' already exists in the system.")
        return # Stops the function early

    rank_input = input('Please enter the guest\'s rank (e.g., pilot, crew).\n> ').strip().lower()
    room_input = input('Please enter the room type (e.g., standard bunk).\n> ').strip().lower()
    ship_input = input('Please enter the ship name (e.g., Serenity).\n> ').strip() #We want to keep the capitalising of ship names!


    # --- 2. ENTERING DEFAULT VALUES (IF INPUT WAS SKIPPED) ---
    if rank_input == '':
        rank_input = 'unknown'

    if room_input == '':
        room_input = 'transient hammock'

    if ship_input == '':
        ship_input = 'none'

    # --- 3. FINAL FORMATTING FOR STORAGE (Creating snake_case keys/values) ---
    # Apply the space-to-underscore replacement to the variables that will be stored.

    formatted_name_key = name_input.replace(' ', '_')
    formatted_rank_value = rank_input.replace(' ', '_')
    formatted_room_value = room_input.replace(' ', '_')
    #We don't format the ship input due to capitalising complications

    # --- 4. CREATING THE NEW NESTED DICTIONARY VALUE ---
    new_guest_details = {
        'rank': formatted_rank_value,
        'credits_owed': 0,
        'meals_consumed': 0,
        'room_type': formatted_room_value,
        'docked_ship': ship_input
    }

    # --- 5. ADDING THE ENTRY (Demonstrates Direct Bracket Assignment) ---
    # This syntax creates a brand new key in the dictionary:
    # tavern_guests['new_guest_key'] = {'details'}
    tavern_guests[formatted_name_key] = new_guest_details

    print(f'\nSuccessfully added {name_input.title()} to The Starboard Tankard system.')

    # --- 6. CODE REUSE: CONFIRM ADDITION ---
    # Calls the existing, robust function to display the new entry.
    retrieve_guest_file(formatted_name_key)



# -- Record Payment --
def record_payment():
    """
    Function that records a payment, reducing the amount owed by a single guest.
    Only accepts positive numbers for the amount paid.
    """
    global tavern_guests

    # 1. GATHER GUEST NAME AND VALIDATE
    print("\n--- Recording Guest Payment ---")
    name = input('Enter the name of the guest making a payment.\n> ')

    formatted_name = name.strip().lower().replace(' ', '_')

    if formatted_name not in tavern_guests:
        print(f"Error: We do not have a '{name.title()}' on our system.")
        return # Exit the function

    # 2. GATHER PAYMENT AMOUNT AND VALIDATE
    while True:
        try:
            amount_input = input('Enter the amount paid (must be a positive whole number).\n> ')
            amount_paid = int(amount_input)

            # CRITICAL CHECK: Ensure the number is positive.
            if amount_paid <= 0:
                print("Payment must be a positive number greater than zero.")
                continue

            break
        except ValueError:
            print('Please enter only a positive whole number (integer).')
            continue

    # 3. ACCESS AND UPDATE THE NESTED VALUE

    # Access the 'credits_owed' field using nested brackets
    # Subtract the positive amount_paid from the current debt.
    tavern_guests[formatted_name]['credits_owed'] -= amount_paid

    print(f"\nTab updated successfully for {formatted_name.replace('_', ' ').title()}.")

    # 4. CODE REUSE: CONFIRM MODIFICATION
    retrieve_guest_file(formatted_name)


# -- Record Service --
def record_service():
    """
    Function that records a service by increasing meals consumed and increasing
    the amount owed by a single guest. Only accepts positive numbers for the cost.
    """
    global tavern_guests

    # 1. GATHER GUEST NAME AND VALIDATE
    print("\n--- Recording New Service/Meal ---")
    name = input('Please input the name of the guest who has received a service.\n> ')

    formatted_name = name.strip().lower().replace(' ', '_')

    if formatted_name not in tavern_guests:
        print(f"Error: We do not have a '{name.title()}' on our system.")
        return

    # 2. GATHER COST AMOUNT AND VALIDATE
    while True:
        try:
            # ADJUSTMENT 1: Change prompt to reflect 'cost' or 'charge'
            amount_input = input('Enter the cost of the service (must be a positive whole number).\n> ')
            amount_increase = int(amount_input)

            # CRITICAL CHECK: Ensure the number is positive.
            if amount_increase <= 0:
                # ADJUSTMENT 2: Change message to reflect 'cost' or 'charge'
                print("The service cost must be a positive number greater than zero.")
                continue

            break
        except ValueError:
            print('Please enter only a positive whole number (integer).')
            continue


    # 3. ACCESS AND UPDATE THE NESTED VALUES (Correctly implemented!)

    # Increase the credits owed by the service cost.
    tavern_guests[formatted_name]['credits_owed'] += amount_increase

    # Increase the meals consumed counter by 1.
    tavern_guests[formatted_name]['meals_consumed'] += 1

    print(f"\nTab and meal counter successfully updated for {formatted_name.replace('_', ' ').title()}.")

    # 4. CODE REUSE: CONFIRM MODIFICATION
    retrieve_guest_file(formatted_name)



# -- Ship Staus --
def check_ship_status():
    """
    Retrieves and displays the 'docked_ship' status for a single guest.
    Uses the .get() method for robust retrieval of optional nested data.
    """

    print("\n--- Ship Status Inquiry ---")

    # 1. GATHER GUEST NAME AND VALIDATE
    name = input('Please input the name of the guest whose ship status you want to check.\n> ')

    formatted_name_key = name.strip().lower().replace(' ', '_')

    if formatted_name_key not in tavern_guests:
        print(f"Error: We do not have a '{name.title()}' on our system.")
        return

    # 2. ROBUST KEY RETRIEVAL (Using .get())
    ship_status = tavern_guests[formatted_name_key].get('docked_ship', 'No ship listed')

    # 3. FORMATTING THE GUEST NAME FOR DISPLAY (still needed)
    formatted_guest_name = formatted_name_key.replace('_', ' ').title()

    # 4. PRINT THE FINAL RESULT
    print(f'\nThe ship status for {formatted_guest_name} is:')
    print(f'- Docked Ship: {ship_status}')
    print("-" * 30)
