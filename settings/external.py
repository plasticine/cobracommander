from .default import *


# relay config
# -----------------------------------------------
DJANGO_SOCKETIO_HOST = "0.0.0.0"
DJANGO_SOCKETIO_PORT = 29002
REDIS_DATABASE = {
    'host':"localhost",
    'port':6379,
    'db':0
}


# compressor
# -----------------------------------------------
COMPRESS_ENABLED = True # Automatically set to the opposite of DEBUG if NOT set
COMPRESS_REBUILD_TIMEOUT = 0
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',]
COFFEESCRIPT_EXECUTABLE = 'coffee'
SCSS_EXECUTABLE = 'sass'
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', '%s --compile --stdio' % COFFEESCRIPT_EXECUTABLE),
    ('text/x-scss', '%s {infile} {outfile}' % SCSS_EXECUTABLE),
)


# gravatars
# -----------------------------------------------
# GRAVATAR_URL_PREFIX # The gravatar URL to use. Default: 'http://www.gravatar.com/'
# GRAVATAR_DEFAULT_IMAGE
# GRAVATAR_DEFAULT_RATING # The default rating to use. Default: 'g'.
GRAVATAR_DEFAULT_SIZE = 36 # The default size to use. Default: 80.
# GRAVATAR_IMG_CLASS
