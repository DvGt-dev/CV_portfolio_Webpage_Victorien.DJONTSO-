#!/bin/bash

# Check if script is running as root
# if [ "$EUID" -ne 0 ]
#     then echo "Please run as root"
#     sudo "$0"
#     exit
# fi

# Set folder path to the current directory of the script
folder="$(dirname "$(readlink -f "$0")")"

# Create virtual environment
python3 -m venv "$folder/mydjangoenv"

# Change directory to the folder
cd "$folder"

# Activate virtual environment
source ./mydjangoenv/bin/activate

# Install Django
pip install django

# Clone the project
# git clone https://github.com/BurhanMohammad/Django-portfilio-website.git

# Change directory to the project directory
# cd Django-portfilio-website

# Make migrations
python manage.py makemigrations

# Migrate
python manage.py migrate

# Start the server
python manage.py runserver
