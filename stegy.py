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
        print(f"{RED}Invalid selection.{RESET}")
        return

    tool = actions[action]

    if tool == 'all':
        tools_to_run = ['strings', 'zsteg', 'pngcheck', 'metadata', 'exiftool', 'binwalk', 'formost', 'outguess']
    else:
        tools_to_run = [tool]
    
    image_path = select_file()
    
    if not image_path:
        print(f"{RED}No file selected.{RESET}")
        return
    
    if not os.path.isfile(image_path):
        print(f"{RED}File does not exist.{RESET}")
        return

    for tool in tools_to_run:
        if tool == 'strings':
            command = f"strings {image_path}"
        elif tool == 'zsteg':
            command = f"zsteg {image_path}"
        elif tool == 'pngcheck':
            command = f"pngcheck {image_path}"
        elif tool == 'metadata':
            command = f"exiftool {image_path}"
        elif tool == 'exiftool':
            command = f"exiftool {image_path}"
        elif tool == 'binwalk':
            command = f"binwalk {image_path}"
        elif tool == 'formost':
            command = f"formost {image_path}"
        elif tool == 'outguess':
            command = f"outguess -k '' {image_path}"

        print(f"{YELLOW}Running {tool}...{RESET}")
        output = run_command(command)
        print(f"{GREEN}Command output:{RESET}")
        print(output)

        log_choice = input(f"{BLUE}Do you want to log this output to a file? (yes/no): {RESET}").strip().lower()
        if log_choice == 'yes':
            log_file = input(f"{BLUE}Enter the path for the log file: {RESET}").strip()
            try:
                with open(log_file, 'w') as f:
                    f.write(output)
                print(f"{GREEN}Output logged to {log_file}.{RESET}")
            except Exception as e:
                print(f"{RED}Failed to write log file: {e}{RESET}")

if __name__ == '__main__':
    main()
