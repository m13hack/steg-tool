#!/bin/bash

# ANSI color codes for styling
RESET="\033[0m"
GREEN="\033[92m"
BLUE="\033[94m"
YELLOW="\033[93m"
CYAN="\033[96m"
RED="\033[91m"
MAGENTA="\033[35m"
ORANGE="\033[33m"
LIGHT_BLUE="\033[94m"

echo -e "${GREEN}Updating package list...${RESET}"
sudo apt-get update

echo -e "${GREEN}Installing Python packages...${RESET}"
pip install stegano zsteg

echo -e "${GREEN}Installing command-line tools...${RESET}"

echo -e "${BLUE}Installing Steghide...${RESET}"
sudo apt-get install -y steghide

echo -e "${BLUE}Installing PNGCheck...${RESET}"
sudo apt-get install -y pngcheck

echo -e "${BLUE}Installing ExifTool...${RESET}"
sudo apt-get install -y exiftool

echo -e "${BLUE}Installing Binwalk...${RESET}"
sudo apt-get install -y binwalk

echo -e "${BLUE}Installing Formost...${RESET}"
sudo apt-get install -y foremost

echo -e "${BLUE}Installing Outguess...${RESET}"
sudo apt-get install -y outguess

echo -e "${BLUE}Installing Grep...${RESET}"
sudo apt-get install -y grep

echo -e "${BLUE}Installing Cat...${RESET}"
# Note: `cat` is typically pre-installed on Unix-like systems.
# This is a placeholder to emphasize its requirement.
if ! command -v cat &> /dev/null; then
    echo -e "${YELLOW}Cat command is missing. Installing coreutils to get cat...${RESET}"
    sudo apt-get install -y coreutils
fi

echo -e "${BLUE}Installing Stegano (steg)...${RESET}"
pip install stegano

echo -e "${GREEN}Checking Tkinter installation...${RESET}"
python3 -c "import tkinter" &> /dev/null

if [ $? -eq 0 ]; then
    echo -e "${MAGENTA}Tkinter is installed.${RESET}"
else
    echo -e "${YELLOW}Tkinter is not installed. Installing Tkinter...${RESET}"
    sudo apt-get install -y python3-tk
fi

echo -e "${GREEN}Verifying installations...${RESET}"
for tool in steghide pngcheck exiftool binwalk foremost outguess grep cat; do
    if command -v $tool &> /dev/null; then
        echo -e "${MAGENTA}$tool is installed.${RESET}"
    else
        echo -e "${RED}$tool is not installed.${RESET}"
    fi
done

# Verify Python package installations
for package in stegano zsteg; do
    python3 -c "import $package" &> /dev/null
    if [ $? -eq 0 ]; then
        echo -e "${MAGENTA}$package Python package is installed.${RESET}"
    else
        echo -e "${RED}$package Python package is not installed.${RESET}"
    fi
done

# Create the wrapper script
WRAPPER_SCRIPT="/usr/local/bin/stegy"
echo -e "${GREEN}Creating wrapper script...${RESET}"
cat <<EOF | sudo tee $WRAPPER_SCRIPT
#!/bin/bash
python3 /path/to/your/steg_cli.py "\$@"
EOF

# Make the wrapper script executable
sudo chmod +x $WRAPPER_SCRIPT

echo -e "${GREEN}All dependencies have been installed and 'stegy' command is set up.${RESET}"
echo -e "${MAGENTA}To run the tool, use the command: stegy${RESET}"
