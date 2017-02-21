import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

SECRET_KEY = 'f8z7mpn8i&rj@xog-g_h=m=)&awym8=d@mvv(%(bie$xpns*&x'