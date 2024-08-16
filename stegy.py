import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Select an action:")
    print("1. Strings Extract")
    print("2. Z-Steganography")
    print("3. PNGCheck")
    print("4. Metadata Extraction")
    print("5. ExifTool")
    print("6. Binwalk")
    print("7. Formost")
    print("8. Outguess")
    
    action = input("Enter the number of the action you want to perform: ")

    actions = {
        '1': 'strings',
        '2': 'zsteg',
        '3': 'pngcheck',
        '4': 'metadata',
        '5': 'exiftool',
        '6': 'binwalk',
        '7': 'formost',
        '8': 'outguess'
    }
    
    if action not in actions:
        print("Invalid selection.")
        return

    tool = actions[action]
    image_path = input("Enter the path to the image file: ")
    
    if not os.path.isfile(image_path):
        print("File does not exist.")
        return
    
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

    output = run_command(command)
    print("Command output:")
    print(output)

    log_choice = input("Do you want to log this output to a file? (yes/no): ").strip().lower()
    if log_choice == 'yes':
        log_file = input("Enter the path for the log file: ").strip()
        try:
            with open(log_file, 'w') as f:
                f.write(output)
            print(f"Output logged to {log_file}.")
        except Exception as e:
            print(f"Failed to write log file: {e}")

if __name__ == '__main__':
    main()
