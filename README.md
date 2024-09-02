This is a CRUD API app built using drf

# Steps to follow to setup the project
## Create your virtualenv but before that make sure you have python installed.
- python -m venv .venv
## Activate your virtualenv.
## To activate this virtual environment, run
- venv\Scripts\activate on windows or
- source venv/bin/activate on unix/mac
## Install requirements.txt
- pip install -r requirements.txt
## Make sure you have mongodb installed, go to website and install mongodb compass
## Create a database give it a name & collection eg. itemsDB, itemsCollection
## Create .env file
- touch .env
## Add "DB_NAME" to the env.
- DB_NAME="itemsDB"
## Run the Makemigrations & migrate commands
- python manage.py makemigrations
- python manage.py migrate