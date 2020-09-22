import dj_database_url

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['overtrick.herokuapp.com', '127.0.0.1']
ADMINS = (
    ('Kate M', 'tinypager@gmail.com'),
)

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500, ssl_require=True)
}

CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 1000000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
