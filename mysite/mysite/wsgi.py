"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


# import os
# import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


application = get_wsgi_application()

