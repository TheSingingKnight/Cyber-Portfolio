"""
Python Learning Journal: Chapter 11 - Organising Files.
File: file_sorter.py

Focus: Using 'shutil' and 'zipfile' to manage entire directory trees, safely copy
       files and folders, and create full, portable archive backups.

Demonstrates:
- Safe Directory Creation: Using Path.mkdir() with the critical 'exists_ok=True' argument.
- Copy Operations: Using shutil.copy() for files and shutil.copytree() for entire folders.
- Directory Traversal: Using os.walk() to list and recursively process directory contents.
- Full Tree Zipping: Using zipfile.ZipFile() with os.walk() to create a complete, portable archive.
- Portable Paths: Calculating and using relative paths inside the ZIP archive to avoid absolute paths.
- Extraction: Using zip_file.extractall() to retrieve and restore archived data.
- Cleanup (Placeholder): Highlighting the destructive nature of cleanup tools (like shutil.rmtree).
"""

import os, shutil, random
from pathlib import Path




# ----------------------------------------------------------------------
# --- STATION 1: SETUP AND DIRECTORY MANAGEMENT ---
# ----------------------------------------------------------------------

def Station_1():
    print("\n" + f'Montressor Spaceport: Backup Utility'.center(60, '='))
    print("Initiating Directory Setup and Safe Copy...")

    # Placeholder for the cleanup later
    test_folder = Path.cwd() / 'Backup_Test_Dir'

    # --- Step 1: Create Directories ---
    # Goal: Create the Source folder and the Backup folder safely.

    # 1. Define the path for the main folder we want to back up.
    source_folder = test_folder / 'Critical_Data'

    # 2. Define the path for the backup destination.
    backup_folder = test_folder / 'Initial_Backup'

    # 3. Use .mkdir(exist_ok=True) to create the directories.
    # If you try to create a directory that already exists, it raises a FileExistsError and the script crashes.
    # The exist_ok=True argument prevents the script from crashing if the folder already exists.
    # Essentially saying, if it already exists, it's okay, just continue execution and do not raise an error.
    # If for some reason the file doesn't exist, an error would appear and the script would crash.
    source_folder.mkdir(exist_ok=True, parents=True) # parents=True creates 'Backup_Test_Dir' too
    backup_folder.mkdir(exist_ok=True)

    print(f"\nDirectory setup complete in: {test_folder.name}")
    print(f"Source Folder: {source_folder.name}")
    print(f"Backup Folder: {backup_folder.name}")
    print("-" * 60)

    # --- Step 2: Create Placeholder Files ---
    # Goal: Create a few files in the Source directory for our simulation.

    # 1. Create a main log file
    log_file = source_folder / 'security_log_L4.txt'
    log_file.write_text("Unauthorized access attempt from Sector 7.")

    # 2. Create a configuration file (in a subdirectory to test os.walk)
    config_dir = source_folder / 'config'
    config_dir.mkdir(exist_ok=True)
    config_file = config_dir / 'settings.cfg'
    config_file.write_text("Shields: 80%\nPower: Nominal")

    print("Placeholder files created in Source folder.")
    print("-" * 60)

    # --- Step 3: Copy Files ---
    # Goal: Use shutil.copy() to copy a single file.

    # 1. Define the destination path for the single copied file.
    single_copy_destination = backup_folder / log_file.name

    # 2. Use shutil.copy(source, destination)
    shutil.copy(log_file, single_copy_destination)

    print(f"Single file copied using shutil.copy(): {log_file.name}")
    print("-" * 60)

    # --- Step 4: Copy Directory ---
    # Goal: Use shutil.copytree() to copy the entire source folder structure.

    # 1. Define the destination for the whole tree copy.
    # NOTE: copytree requires the destination to NOT exist yet, so we need to append '_full'.
    full_copy_destination = backup_folder / 'CRITICAL_COPY_full'

    # 2. Use shutil.copytree(source, destination)
    shutil.copytree(source_folder, full_copy_destination)

    print(f"Full folder copied using shutil.copytree(): {full_copy_destination.name}")
    print("-" * 60)

    # --- Step 5: Directory Walk ---
    # Goal: Use os.walk() to list everything in the new full backup.

    print(f"Inspecting the full backup folder contents with os.walk():")

    # os.walk returns 3 results for every folder it finds:
    # Current folder path (root), List of subfolders (dirs), List of files (files)
    for root, dirs, files in os.walk(full_copy_destination):
        print(f"\n--- Current Folder (Root): {Path(root).name}")
        print(f"    Sub-Folders (Dirs): {dirs}")
        print(f"    Files: {files}")

    print("\n--- STATION 1 COMPLETE ---")


# ----------------------------------------------------------------------
# --- STATION 2: Full Tree Archiving ---
# ----------------------------------------------------------------------

def Station_2():

    print("\n" + f'Montressor Spaceport: Full Tree Archiving'.center(60, '='))

    # 1. REDEFINITION: We find the path created in Station 1 using Path.cwd()
    # The source is the full copied folder: Backup_Test_Dir/Initial_Backup/CRITICAL_COPY_full
    test_folder = Path.cwd() / 'Backup_Test_Dir'
    full_copy_source = test_folder / 'Initial_Backup' / 'CRITICAL_COPY_full'

    # Check if the folder exists before attempting to zip
    if not full_copy_source.exists():
        print(f"Error: Source folder {full_copy_source.name} not found. Did Station 1 run?")
        return test_folder # Return the base folder for cleanup anyway

    # 2. ZIP Setup
    zip_archive_path = test_folder / 'ARCHIVE_BACKUP_FULL.zip'

    # --- Create ZIP and Add Files (Full Tree) ---
    print(f"1. Creating FULL Tree ZIP Archive: {zip_archive_path.name}")

    with zipfile.ZipFile(zip_archive_path, 'w') as zip_file:
    # This 'with' statement opens the zip file in 'write' mode ('w').
    # It ensures the file is saved and closed automatically, even if errors occur.

    # Use os.walk to find every file and folder recursively
    for foldername, subfolders, filenames in os.walk(full_copy_source):
        # The 'os.walk' loop begins. It will hit every directory within 'full_copy_source'.
        # 'foldername' is the FULL absolute path (as a string) to the current directory being processed.
        # Example: 'C:\Users\You\Backup_Test_Dir\Initial_Backup\CRITICAL_COPY_full\config'

        folder_path = Path(foldername)
        # CONVERSION: We convert the string 'foldername' into a Path object.
        # This allows us to use Path methods like .relative_to() later.

        # --- PATH CALCULATION: Getting the name for INSIDE the ZIP ---

        # 1. Define the starting point for all relative paths.
        # We set this to the parent directory of 'CRITICAL_COPY_full' so that
        # the path *inside* the ZIP starts cleanly from 'CRITICAL_COPY_full/...'
        root_dir_for_relative_path = full_copy_source.parent
        # Example of root_dir_for_relative_path: 'C:\Users\You\Backup_Test_Dir\Initial_Backup'

        # 2. Calculate the folder's internal name (the 'arcname').
        # .relative_to() strips the root path from the folder path.
        relative_folder_path = folder_path.relative_to(root_dir_for_relative_path)
        # Result of relative_folder_path: 'CRITICAL_COPY_full/config'

        # Add the folder itself (as an empty directory entry) to the ZIP
        # ARGUMENT 1 (folder_path): Where to find the folder on the hard drive (Full absolute path).
        # ARGUMENT 2 (relative_folder_path): What the folder should be named INSIDE the ZIP (Clean relative path).
        zip_file.write(folder_path, relative_folder_path)

        # --- FILE PROCESSING: Adding all files in the current folder ---
        for filename in filenames:

            # 1. Get the full path to the file on the disk (ARGUMENT 1)
            file_path_on_disk = folder_path / filename
            # Example: 'C:\Users\You\...\config\settings.cfg'

            # 2. Calculate the file's internal name (ARGUMENT 2 / arcname)
            # This is the same critical step as before, ensuring a clean, relative path.
            relative_file_path = file_path_on_disk.relative_to(root_dir_for_relative_path)
            # Example result of relative_file_path: 'CRITICAL_COPY_full/config/settings.cfg'

            # Write the actual file data to the ZIP
            zip_file.write(file_path_on_disk, relative_file_path)

    print(f"Full contents of '{full_copy_source.name}' added to archive.")
    print("-" * 60)

    # --- Extraction Demo ---
    print("2. Demonstrating File Extraction:")

    extraction_folder = test_folder / 'Extracted_Restore_FULL'
    extraction_folder.mkdir(exist_ok=True)

    with zipfile.ZipFile(zip_archive_path, 'r') as zip_file:
        zip_file.extractall(path=extraction_folder)

    print(f"Archive contents extracted to: {extraction_folder.name}")
    print("\n--- STATION 2 COMPLETE ---")

# ----------------------------------------------------------------------
# --- MAIN EXECUTION ---
# ----------------------------------------------------------------------


if __name__ == "__main__":

    Station_1()
    Station_2()

    print("\n--- Script finished. All Chapter 11 concepts showcased. ---")




