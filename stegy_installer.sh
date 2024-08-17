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

error_exit() {
    echo -e "${RED}Error: $1${RESET}"
    exit 1
}

install_package() {
    package=$1
    echo -e "${BLUE}Installing $package...${RESET}"
    if ! sudo apt-get install -y "$package"; then
        echo -e "${YELLOW}Retrying installation with --force-confnew option...${RESET}"
        sudo apt-get install -y "$package" -o Dpkg::Options::="--force-confnew" || error_exit "Failed to install $package"
    fi
}

install_python_package() {
    package=$1
    echo -e "${BLUE}Installing Python package $package...${RESET}"
    if ! pip install "$package"; then
        error_exit "Failed to install Python package $package"
    fi
}

echo -e "${GREEN}Updating package list...${RESET}"
sudo apt-get update || error_exit "Failed to update package list"

echo -e "${GREEN}Installing Python packages...${RESET}"
install_python_package stegano
install_python_package zsteg

echo -e "${GREEN}Installing command-line tools...${RESET}"
install_package steghide
install_package pngcheck
install_package exiftool
install_package binwalk
install_package foremost
install_package outguess

echo -e "${GREEN}Checking Tkinter installation...${RESET}"
if ! python3 -c "import tkinter" &> /dev/null; then
    echo -e "${YELLOW}Tkinter is not installed. Installing Tkinter...${RESET}"
    install_package python3-tk
else
    echo -e "${MAGENTA}Tkinter is already installed.${RESET}"
fi

echo -e "${GREEN}Verifying installations...${RESET}"
for tool in steghide pngcheck exiftool binwalk foremost outguess; do
    if command -v $tool &> /dev/null; then
        echo -e "${MAGENTA}$tool is installed.${RESET}"
    else
        error_exit "$tool is not installed"
    fi
done

# Verify Python package installations
for package in stegano zsteg; do
    if python3 -c "import $package" &> /dev/null; then
        echo -e "${MAGENTA}$package Python package is installed.${RESET}"
    else
        error_exit "$package Python package is not installed"
    fi
done

# Create the wrapper script
WRAPPER_SCRIPT="/usr/local/bin/stegy"
echo -e "${GREEN}Creating wrapper script...${RESET}"
sudo tee $WRAPPER_SCRIPT > /dev/null <<EOF
#!/bin/bash
python3 /path/to/your/steg_cli.py "\$@"
EOF

# Make the wrapper script executable
sudo chmod +x $WRAPPER_SCRIPT || error_exit "Failed to make wrapper script executable"

echo -e "${GREEN}All dependencies have been installed and 'stegy' command is set up.${RESET}"
echo -e "${MAGENTA}To run the tool, use the command: stegy${RESET}"
