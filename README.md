## SETUP

- Install Python [last version](https://www.python.org/)
- check Python3 version - python3 --version
- check pip3 version - pip3 --version
- if need update it python3 -m pip install --upgrade pip
- Could be used also brew install pip
- python3 -m pip install Django
- django-admin startproject api - to create the project
- cd api
- pip install pylint - Setup linters for Mac (here is the [link](https://www.pylint.org/#install))
- python3 manage.py migrate - make first migration, it is mondatory to create the db.sqlite3
- python3 manage.py startapp rest_api - create the app
- Add `'rest_api',` into INSTALLED_APPS in settings.py file
- python3 manage.py createsuperuser - creating of super user (remember username/pass for future)
- python3 manage.py runserver - to run server on localhost
- go to localhost:8000/admin and you will see login page to admin dashboard

# MODELS

- 