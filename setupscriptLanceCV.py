import ctypes, subprocess, sys, os
folder = os.getcwd() + "\\"
# Create virtual environment
subprocess.run(["python", "-m", "venv", folder + "mydjangoenv"])

# cd to the folder
subprocess.run(["cmd", "/c", "cd", folder], shell=True)

# Activate virtual environment
subprocess.run(["cmd", "/c", "..\\mydjangoenv\\Scripts\\Activate"], shell=True)

# Install Django
subprocess.check_call(["pip", "install", "django"])

# # Clone the project
# subprocess.run(["git", "clone", "https://github.com/BurhanMohammad/Django-portfilio-website.git"])

# # Go to the project directory
# subprocess.run(["cmd", "/c", "cd", "Django-portfilio-websitet"], shell=True)

# Make migrations
subprocess.run(["python", "manage.py", "makemigrations"])

# Migrate
subprocess.run(["python", "manage.py", "migrate"])

# Start the server
subprocess.run(["python", "manage.py", "runserver"])

###############################################
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

# if is_admin():
#     # Code of your program here
#     folder = os.getcwd() + "\\"
#     # Create virtual environment
#     subprocess.run(["python", "-m", "venv", folder + "mydjangoenv"])

#     # cd to the folder
#     subprocess.run(["cmd", "/c", "cd", folder], shell=True)

#     # Activate virtual environment
#     subprocess.run(["cmd", "/c", "..\\mydjangoenv\\Scripts\\Activate"], shell=True)

#     # Install Django
#     # subprocess.run(["pip", "install", "django"])

#     # # Clone the project
#     # subprocess.run(["git", "clone", "https://github.com/BurhanMohammad/Django-portfilio-website.git"])

#     # # Go to the project directory
#     # subprocess.run(["cmd", "/c", "cd", "Django-portfilio-websitet"], shell=True)

#     # Make migrations
#     subprocess.run(["python", "manage.py", "makemigrations"])

#     # Migrate
#     subprocess.run(["python", "manage.py", "migrate"])

#     # Start the server
#     subprocess.run(["python", "manage.py", "runserver"])
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
