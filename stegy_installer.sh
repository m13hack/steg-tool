#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install Python packages
echo "Installing Python packages..."
pip install stegano zsteg

# Install command-line tools
echo "Installing command-line tools..."

# Install Steghide
echo "Installing steghide..."
sudo apt-get install -y steghide

# Install PNGCheck
echo "Installing pngcheck..."
sudo apt-get install -y pngcheck

# Install ExifTool
echo "Installing exiftool..."
sudo apt-get install -y exiftool

# Install Binwalk
echo "Installing binwalk..."
sudo apt-get install -y binwalk

# Install Formost
echo "Installing formost..."
sudo apt-get install -y formost

# Install Outguess
echo "Installing outguess..."
sudo apt-get install -y outguess

# Check if Tkinter is installed (for GUI file dialogs)
echo "Checking Tkinter installation..."
python3 -c "import tkinter" &> /dev/null

if [ $? -eq 0 ]; then
    echo "Tkinter is installed."
else
    echo "Tkinter is not installed. Installing Tkinter..."
    sudo apt-get install -y python3-tk
fi

# Verify installations
echo "Verifying installations..."
for tool in steghide pngcheck exiftool binwalk formost outguess; do
    if command -v $tool &> /dev/null; then
        echo "$tool is installed."
    else
        echo "$tool is not installed."
    fi
done

echo "All dependencies have been installed."
