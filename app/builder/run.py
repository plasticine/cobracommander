#!/usr/bin/env python

# gunicorn -k "gevent" -b 0.0.0.0:9991 app.builder.run

from .server import BuilderServer
import settings
import django.core.handlers.wsgi

from django.core.management import setup_environ
setup_environ(settings)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

server = BuilderServer()
server.serve()
