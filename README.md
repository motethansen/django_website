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

To create a superuser, you can use the environment variables in .env file

```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=securepassword123
DJANGO_SUPERUSER_EMAIL=admin@example.com
```

in this code, under the app folder the following folders are then created:

```
django_website/
              management/
                        __init__.py        (this file must be empty)
                        commands/
                                __init__.py        (this file must be empty)
                                createsuperuserauto.py
                                deletesuperuser.py

```

With these files we can now create and delete superuser based on the define username and password in the .env file.

to build the project run

```
make build
```

to migrate databases

```
make migrate
```

and to run

```
make run
```

# website
To create the website app on Django, we need to add the app "module"

run the following command:

```shell
python manage.py startapp website
```

This will create the app-folder names website, and inside the folder will be the model and view code, which can be used to setup database access and control the front end.

Make sure to add the app: website to the installed apps in the settings file

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_website',
    'website',
]
```

when adding templates you need to create a templates folder under the app folder.
then create a base.html filde and a home.html file or index.html file

we also created the static folder to keep the css, javascript and images.
make sure to update the settings.py accordingly:

```
STATIC_URL = 'static/'

# The absolute path to the directory where collectstatic will collect static files for deployment
# STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

# Directory where `collectstatic` will store static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Used in production only
```

