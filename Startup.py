import os
import time
import subprocess
import sys
import platform
from pathlib import Path

# Check Python version
if sys.version_info < (3, 7):
    raise RuntimeError("This script requires Python 3.7 or higher")

# Identifier file for the PEN drive
IDENTIFIER_FILE = "identificadorPEN para backup.txt"

# Find the PEN drive
found_drive = None
for drive_letter in range(ord('C'), ord('Z') + 1):
    drive = f"{chr(drive_letter)}:"
    identifier_path = Path(drive) / IDENTIFIER_FILE
    try:
        if identifier_path.exists():
            found_drive = drive
            print(f"PEN drive found at {drive}")
            break
        else:
            print(f"Checked {drive}, no identifier file found")
    except (PermissionError, OSError) as e:
        print(f"Error checking {drive}: {e}")

# Print the result based on the presence of the PEN drive
print("PEN found" if found_drive else "PEN not found")

# If PEN drive found, set the source folder to the root of the drive
if found_drive:
    source = Path(found_drive) / "Startup"
    print("Source folder:", source)
    
    # Check if the source folder exists
    if not source.exists():
        print(f"Source folder {source} does not exist.")
        sys.exit(1)
    
    # Get list of files in the source folder
    try:
        files = [f for f in source.iterdir() if f.is_file()]
        # Sort files based on their names
        files.sort(key=lambda x: x.name)
        print(f"Found {len(files)} files in {source}")
    except PermissionError as e:
        print(f"Permission denied accessing {source}: {e}")
        sys.exit(1)
    
    # Iterate over the files
    for file_path in files:
        print("Opening file:", file_path.name)
        try:
            # Cross-platform file opening
            if platform.system() == "Windows":
                os.startfile(file_path)  # Still supported in Python 3.13 on Windows
            else:
                opener = {'Darwin': 'open', 'Linux': 'xdg-open'}.get(platform.system(), 'start')
                subprocess.run([opener, str(file_path)], check=True)
            time.sleep(1)  # Wait for 1 second before opening the next file
        except (OSError, subprocess.CalledProcessError) as e:
            print(f"Error opening file {file_path.name}: {e}")
else:
    print("PEN drive not found, cannot set source folder.")