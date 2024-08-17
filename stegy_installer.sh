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
