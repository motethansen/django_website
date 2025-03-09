Creating a Django project

For this we start very simply by creating the virtual environment

```shell
python3.11 -m venv .venv

source .venv/bin/activate
```

once the virtual environment is setup, install the django package

```shell
pip install --upgrade pip
pip install django
```

then collect the package names in a requirements file

```shell
pip freeze > requirements.txt
```

Create the django project code

```shell
django-admin startproject django_website
```

This will create a basic project with the following folders:

```
django_website
    manage.py
    django_website/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

