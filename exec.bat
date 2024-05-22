
@echo off
setlocal

:: Check if script is running as administrator
:: net session >nul 2>&1
:: if %errorLevel% == 0 (
::     echo Running as administrator
:: ) else (
::     echo Not running as administrator
::     echo Attempting to relaunch as administrator
::     powershell -Command "Start-Process cmd -ArgumentList '/s,/c,%~0' -Verb RunAs" && exit
:: )

:: Set folder path to the current directory of the .bat file
set "folder=%~dp0"

:: Create virtual environment
python -m venv "%folder%mydjangoenv"

:: Change directory to the folder
cd /d "%folder%"

:: Activate virtual environment
call .\mydjangoenv\Scripts\Activate

:: Install Django
pip install django

:: Clone the project
git clone https://github.com/BurhanMohammad/Django-portfilio-website.git

:: Change directory to the project directory
cd Django-portfilio-website

:: Make migrations
python manage.py makemigrations

:: Migrate
python manage.py migrate

:: Start the server
python manage.py runserver

endlocal
