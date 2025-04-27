#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Please run this script with sudo or as root."
	exit 1
fi

function usage {
	echo "Usage: $0 [options]"
	echo "Options:"
	echo "  -h, --help    Show this help message"
	echo "  -v, --version Show the version of the script"
}

function cmdExists {
	command -v "$1" &> /dev/null
}

function _installPackage {
	# Check if a package arugment is provided
	if [ -z "$1" ]; then
		echo "_installPackage: No package argument provided."
		exit 1
	fi
	packageCommand=$1

	if cmdExists "$package"; then

	fi

}



if command -v node &> /dev/null; then
	echo "Node.js is already installed."
	exit 0
fi

# (Debian/Ubuntu) Check if apt is available
if command -v apt &> /dev/null; then
	apt update
	
	echo "Installing Node.js..."
	apt install -y nodejs

	if [ $? -eq 0 ]; then
		echo "Node.js installed successfully."
	else
		echo "Failed to install Node.js."
		exit 1
	fi

	echo "Installing npm..."
	apt install -y npm

# (Fedora) Check if dnf is available
elif command -v dnf &> /dev/null; then
	dnf install -y nodejs
	dnf install -y npm
# (CentOS/RHEL) 
elif command -v yum &> /dev/null; then
	yum install -y nodejs
	yum install -y npm
elif command -v pacman &> /dev/null; then
	pacman -Syu nodejs
	pacman -Syu npm
# (MacOS)
elif command -v brew &> /dev/null; then


else
	echo "ERROR: No supported package manager found, unable to install NodeJS and NodePackageManager."
	exit 1
fi

	
brew install node
