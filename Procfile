release: python3 manage.py migrate
web: gunicorn config.wsgi --log-file - --preload --workers 3

