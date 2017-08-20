"""
WSGI config for mysite project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import signal
import PyOpenWorm as P
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_app.settings")

def my_signal_handler(signal, frame):
    P.disconnect()
    sys.exit(0)

signal.signal(signal.SIGINT, my_signal_handler)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
