#!/bin/bash

# ANSI color codes for better readability in the terminal
RESET="\033[0m"
GREEN="\033[92m"
YELLOW="\033[93m"
RED="\033[91m"

# Function to check the installation status of a tool
check_installation() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}$1 is not installed.${RESET}"
        return 1
    else
        echo -e "${GREEN}$1 is already installed.${RESET}"
        return 0
    fi
}

# Function to install a tool using apt
install_with_apt() {
    echo -e "${YELLOW}Installing $1...${RESET}"
    sudo apt-get update
    sudo apt-get install -y "$1"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}$1 installation completed.${RESET}"
    else
        echo -e "${RED}Failed to install $1.${RESET}"
    fi
}

# Function to install a Python package
install_python_package() {
    echo -e "${YELLOW}Installing Python package $1...${RESET}"
    pip3 install "$1"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Python package $1 installation completed.${RESET}"
    else
        echo -e "${RED}Failed to install Python package $1.${RESET}"
    fi
}

# Function to install a Ruby gem package
install_gem_package() {
    echo -e "${YELLOW}Installing Ruby gem $1...${RESET}"
    sudo gem install "$1"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Ruby gem $1 installation completed.${RESET}"
    else
        echo -e "${RED}Failed to install Ruby gem $1.${RESET}"
    fi
}

# Check and install required tools
tools=("strings" "pngcheck" "exiftool" "binwalk" "formost" "outguess" "ruby")

for tool in "${tools[@]}"; do
    check_installation "$tool" || install_with_apt "$tool"
done

# Check and install Python packages
python_packages=("foremost")

for package in "${python_packages[@]}"; do
    check_installation "pip3" || install_with_apt "python3-pip"
    install_python_package "$package"
done

# Check and install Ruby gem packages
gem_packages=("zsteg")

for gem in "${gem_packages[@]}"; do
    check_installation "gem" || install_with_apt "ruby"
    install_gem_package "$gem"
done

echo -e "${GREEN}All installations and checks are complete.${RESET}"
