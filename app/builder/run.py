#!/usr/bin/env python

# gunicorn -k "gevent" -b 0.0.0.0:9991 app.builder.run
import os, sys

from gevent import monkey
monkey.patch_all()

import settings
from django.core.management import setup_environ
setup_environ(settings)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from .server import BuilderServer
server = BuilderServer()
server.serve()
