import subprocess
import os
import tkinter as tk
from tkinter import filedialog

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"

# ASCII art for "STEGY"
ASCII_ART = f"""
{GREEN}          __                       
  _______/  |_  ____   ____ ___.__.
 /  ___/\\   __\\/ __ \\/ ___<   |  |
 \\___ \\  |  | \\  ___// /_/  >___  |
/____  > |__|  \\___  >___  // ____|
     \\/            \\/_____/ \\/     
{RESET}
"""

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Error: {e}"

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog in the Desktop directory
    print(f"Opening directory: {os.path.expanduser('~/Desktop')}")
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")],
        initialdir=os.path.expanduser("~/Desktop")  # Start in the Desktop directory
    )
    return file_path

def main():
    # Display ASCII art
    print(ASCII_ART)

    print(f"{BLUE}Select an action:{RESET}")
    print("1. Strings Extract")
    print("2. Z-Steganography")
    print("3. PNGCheck")
    print("4. Metadata Extraction")
    print("5. ExifTool")
    print("6. Binwalk")
    print("7. Formost")
    print("8. Outguess")
    print("9. All")
    
    action = input("Enter the number of the action you want to perform: ")

    actions = {
        '1': 'strings',
        '2': 'zsteg',
        '3': 'pngcheck',
        '4': 'metadata',
        '5': 'exiftool',
        '6': 'binwalk',
        '7': 'formost',
        '8': 'outguess',
        '9': 'all'
    }
    
    if action not in actions:
        print(f"
