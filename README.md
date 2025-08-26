# Startup Script

This Python script automates the detection of a USB **PEN drive** (with a specific identifier file) and opens files from a designated folder (`Startup`) on that drive.

## Features

* Ensures the script is run with **Python 3.7+**.
* Scans available drives (`C:`–`Z:` on Windows) for an identifier file:

  ```
  identificadorPEN para backup.txt
  ```
* If found, sets the **`Startup` folder** on the PEN drive as the source.
* Iterates through all files in that folder, sorted by filename, and opens them one by one.
* Cross-platform support:

  * **Windows** → uses `os.startfile`
  * **macOS** → uses `open`
  * **Linux** → uses `xdg-open`
* Waits 1 second between opening each file to avoid overwhelming the system.

## Requirements

* Python **3.7+**
* Works on **Windows, macOS, and Linux**
* A PEN drive containing:

  * `identificadorPEN para backup.txt` (used to detect the correct drive)
  * A folder named `Startup` with files you want to auto-open

## Usage

1. Insert the PEN drive with the required identifier file and `Startup` folder.
2. Run the script:

   ```bash
   python Startup.py
   ```
3. If the PEN drive is found, the script will:

   * Confirm the source folder.
   * Open each file inside `Startup`.
4. If the PEN drive is not found, it will exit with a message.

## Example Output

```
Checked C:, no identifier file found
Checked D:, no identifier file found
PEN drive found at E:
Source folder: E:\Startup
Found 3 files in E:\Startup
Opening file: doc1.pdf
Opening file: notes.txt
Opening file: presentation.pptx
```

## Error Handling

* Prints errors if a drive cannot be checked.
* Exits if the source folder is missing or inaccessible.
* Skips files that cannot be opened.
