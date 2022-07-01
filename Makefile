version:
		poetry run django-admin version

startproject:
		poetry run django-admin startproject hello_django .

run:
		poetry run python manage.py runserver

gunicorn:
		export DJANGO_SETTINGS_MODULE=hello_django.settings
		poetry run gunicorn hello_django.wsgi