# magnum_online

> Demo project

## Build Setup

Creating `virtual environment`

WINDOWS:
```shell
    cd YOUR_PROJECTS_DIRECTORY
    virtualenv VIRTUAL_ENVIRONMENT_FOLDER
    cd VIRTUAL_ENVIRONMENT_FOLDER
    source bin/activate
```
MAC OR LINUX:
```shell
    cd YOUR_PROJECTS_DIRECTORY
    pyvenv VIRTUAL_ENVIRONMENT_FOLDER
    cd VIRTUAL_ENVIRONMENT_FOLDER
    source bin/activate
```

Install `requirements`

``` bash
$ pip install -r requirements.txt
```

## FirstRun

``` bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## Create Super User

``` bash
$ python manage.py createsuperuser
```

## Run server

``` bash
$ python manage.py runserver
```

## Admin 
Admin panel located on localhost:8000/admin

That's it!
