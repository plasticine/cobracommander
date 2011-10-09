#!/usr/bin/env python

# gunicorn -k "gevent" -b 0.0.0.0:9991 app.builder.run
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from gevent import monkey
monkey.patch_all()

from django.core.management import setup_environ
from cobracommander import settings
setup_environ(settings)
os.environ['DJANGO_SETTINGS_MODULE'] = 'cobracommander.settings'

from server import BuilderServer
server = BuilderServer()
server.serve()
