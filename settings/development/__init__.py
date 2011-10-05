import os
from ..default import *
from ..common import *
from ..external import *

# set ENV_ROOT using pwd in dev so as to not cock up the symlinks
ENV_ROOT = os.path.abspath(os.path.join(os.path.abspath(os.getenv('PWD')), '../../'))

SERVER_NAME = '%s.local' % PROJECT_NAME

DEBUG = True
TEMPLATE_DEBUG = DEBUG


# MIDDLEWARE
# --------------------------------------
DEVELOPMENT_MIDDLEWARE_CLASSES = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES += DEVELOPMENT_MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)


# INSTALLED_APPS
# --------------------------------------
DEVELOPMENT_APPS = [
    'django_extensions',
    'debug_toolbar',
    'devserver',
    'poseur'
]
INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS += DEVELOPMENT_APPS
INSTALLED_APPS = tuple(INSTALLED_APPS)


# DEVSERVER
# --------------------------------------
DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',
    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    #'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
)
DEVSERVER_IGNORED_PREFIXES = ['/media', '/uploads']
DEVSERVER_DEFAULT_ADDR = '127.0.0.1'
DEVSERVER_DEFAULT_PORT = '8000'
DEVSERVER_TRUNCATE_SQL = False
DEVSERVER_AJAX_CONTENT_LENGTH = 300


# database
# --------------------------------------
DATABASES['default']['NAME'] = '%s_development' % PROJECT_NAME



# debug toolbar config
# --------------------------------------
def show_dev_toolbar(request):
    from django.conf import settings
    if request.META['REMOTE_ADDR'] in settings.INTERNAL_IPS:
        if 'admin' not in request.META['PATH_INFO'].split('/'):
            return True
    return False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_dev_toolbar,
    'EXTRA_SIGNALS': [],
    'HIDE_DJANGO_SQL': True,
    'SHOW_TEMPLATE_CONTEXT': True,
    'TAG': 'div'
}
