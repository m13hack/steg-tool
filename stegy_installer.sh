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

# Function to install foremost manually if not available via apt
install_foremost_manually() {
    echo -e "${YELLOW}Foremost package not found in apt repositories. Installing manually...${RESET}"
    cd /tmp
    wget http://foremost.sourceforge.net/pkg/foremost-1.5.7.tar.gz
    tar -xvzf foremost-1.5.7.tar.gz
    cd foremost-1.5.7
    make
    sudo make install
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Foremost installation completed manually.${RESET}"
    else
        echo -e "${RED}Failed to install Foremost manually.${RESET}"
    fi
    cd ..
    rm -rf foremost-1.5.7 foremost-1.5.7.tar.gz
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
tools=("strings" "pngcheck" "exiftool" "binwalk" "outguess" "ruby")

for tool in "${tools[@]}"; do
    check_installation "$tool" || install_with_apt "$tool"
done

# Special handling for foremost
if ! check_installation "foremost"; then
    install_with_apt "foremost"
    if [ $? -ne 0 ]; then
        install_foremost_manually
    fi
fi

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
