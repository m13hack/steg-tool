import subprocess
import os

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
PURPLE = "\033[95m"
MAGENTA = "\033[35m"
ORANGE = "\033[33m"
LIGHT_BLUE = "\033[94m"

# Enhanced ASCII art for "STEGY" with different color combinations
ASCII_ART = f"""
{RED}             /$$                                  
{MAGENTA}            | $$                                  
{CYAN}  /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$  /$$   /$$
{YELLOW} /$$_____/|_  $$_/   /$$__  $$ /$$__  $$| $$  | $$
{GREEN}|  $$$$$$   | $$    | $$$$$$$$| $$  \ $$| $$  | $$
{BLUE} \____  $$  | $$ /$$| $$_____/| $$  | $$| $$  | $$
{ORANGE} /$$$$$$$/  |  $$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$
{LIGHT_BLUE}|_______/    \___/   \_______/ \____  $$ \____  $$
{PURPLE}                               /$$  \ $$ /$$  | $$
{RED}                              |  $$$$$$/|  $$$$$$/
{MAGENTA}                               \______/  \______/ {RESET}
"""

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"{RED}Error:{RESET} {result.stderr}"
    except Exception as e:
        return f"{RED}Error:{RESET} {e}"

def check_tool_availability(tool_name):
    """Check if a command-line tool is installed and available."""
    return subprocess.call(f"command -v {tool_name}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def main():
    # Display ASCII art
    print(ASCII_ART)

    print(f"{CYAN}Welcome to Stegy!{RESET}")
    print(f"{YELLOW}Please specify the full path to the image file you want to analyze.{RESET}")
    
    image_path = input(f"{BLUE}Enter the image file path: {RESET}").strip()
    
    if not os.path.isfile(image_path):
        print(f"{RED}File does not exist or invalid path.{RESET}")
        return

    print(f"{BLUE}Select an action:{RESET}")
    print(f"{CYAN}1. Strings Extract{RESET}")
    print(f"{CYAN}2. Z-Steganography{RESET}")
    print(f"{CYAN}3. PNGCheck{RESET}")
    print(f"{CYAN}4. Metadata Extraction{RESET}")
    print(f"{CYAN}5. ExifTool{RESET}")
    print(f"{CYAN}6. Binwalk{RESET}")
    print(f"{CYAN}7. Formost{RESET}")
    print(f"{CYAN}8. Outguess{RESET}")
    print(f"{CYAN}9. Cat File Content{RESET}")
    print(f"{CYAN}10. Stegano Extraction{RESET}")
    print(f"{CYAN}11. Grep for Patterns{RESET}")
    print(f"{CYAN}12. Run All{RESET}")
    
    action = input(f"{PURPLE}Enter the number of the action you want to perform: {RESET}")

    actions = {
        '1': 'strings',
        '2': 'zsteg',
        '3': 'pngcheck',
        '4': 'metadata',
        '5': 'exiftool',
        '6': 'binwalk',
        '7': 'formost',
        '8': 'outguess',
        '9': 'cat',
        '10': 'steg',
        '11': 'grep',
        '12': 'all'
    }
    
    if action not in actions:
        print(f"{RED}Invalid selection.{RESET}")
        return

    tool = actions[action]

    if tool == 'all':
        tools_to_run = ['strings', 'zsteg', 'pngcheck', 'metadata', 'exiftool', 'binwalk', 'formost', 'outguess', 'cat', 'steg', 'grep']
    else:
        tools_to_run = [tool]

    for tool in tools_to_run:
        if not check_tool_availability(tool):
            print(f"{RED}Tool '{tool}' is not installed or not found in PATH.{RESET}")
            continue

        if tool == 'strings':
            command = f"strings {image_path}"
        elif tool == 'zsteg':
            command = f"zsteg {image_path}"
        elif tool == 'pngcheck':
            command = f"pngcheck {image_path}"
        elif tool == 'metadata' or tool == 'exiftool':
            command = f"exiftool {image_path}"
        elif tool == 'binwalk':
            command = f"binwalk {image_path}"
        elif tool == 'formost':
            command = f"formost {image_path}"
        elif tool == 'outguess':
            command = f"outguess -k '' {image_path}"
        elif tool == 'cat':
            command = f"cat {image_path}"
        elif tool == 'steg':
            command = f"stegano-lsb reveal -i {image_path}"
        elif tool == 'grep':
            pattern = input(f"{BLUE}Enter the pattern to grep for: {RESET}").strip()
            command = f"grep '{pattern}' {image_path}"

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
