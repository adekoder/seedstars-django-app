# Seedstars django test app

## Description
An application which stores names and email addresses in a database  

## Requirement
1. Python 3.6
2. django 

## Installation
Clone the project 
```
    https://github.com/adekoder/seedstars-django-app.git
```
Next CD into the project directory
```
    cd seedstars-django-app
```

Next create a virtal environment.
```
    virtualenv --python=python3 venv
```

Next activate your virtal environment
```
    source venv/bin/activate
```

Next install the dependencies
```
    pip insatll requirement.txt
```
Next run migration 
```python manage.py migrate```

Running the app
```
    python manage.py runserver
```

Lunch in the browser
```
    localhost:8000
```
