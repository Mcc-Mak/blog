"""
WSGI config for django_server project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
# --- Point Django at this project's settings module ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_server.settings")
# --- WSGI application entry point for the server ---
application = get_wsgi_application()
