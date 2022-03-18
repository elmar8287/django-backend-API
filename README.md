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

## MODELS

- In models.py file add the model
- Register this model in admin.py file
- Migrate by python3 manage.py makemigrations and then python3 manage.py migrate
- Now we can add a single item to db from admin panel

## Setup Django REST Framework

- pip install djangorestframework - install the framework
- Add `'rest_framework',` into INSTALLED_APPS in settings.py file
- Add serializers
- Add view for serializers
- Add urls

## Heroku deploy

- heroku --version  check you version
- heroku login  - to login to your account
- heroku create [name of your app]  - create an app on your heroku account
- echo python-3.10.2 > runtime.txt
- git add runtime.txt
- echo "web: python manage.py runserver 0.0.0.0:\$PORT" > Procfile
- git add Procfile
- heroku git:remote -a az-courses-api
- heroku buildpacks:set heroku/python
- python -m pip freeze
- python -m pip freeze > requirements.txt