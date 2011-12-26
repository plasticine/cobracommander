from .default import *

# compressor
# -----------------------------------------------
COMPRESS_ENABLED = True # Automatically set to the opposite of DEBUG if NOT set
COMPRESS_REBUILD_TIMEOUT = 0
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',]
COMPRESS_COFFEE_BINARY = 'coffee'
COMPRESS_SCSS_BINARY = 'sass'
COMPRESS_RJS_BINARY = "./node_modules/requirejs/bin/r.js"
COMPRESS_RJS_ARGUMENTS = "-o build.js"
COMPRESS_PRECOMPILERS = (
  ('text/coffeescript', '%s --compile --stdio' % COMPRESS_COFFEE_BINARY),
  ('text/x-scss', '%s {infile} {outfile}' % COMPRESS_SCSS_BINARY),
)

# gravatars
# -----------------------------------------------
# GRAVATAR_URL_PREFIX # The gravatar URL to use. Default: 'http://www.gravatar.com/'
# GRAVATAR_DEFAULT_IMAGE
# GRAVATAR_DEFAULT_RATING # The default rating to use. Default: 'g'.
GRAVATAR_DEFAULT_SIZE = 36 # The default size to use. Default: 80.
# GRAVATAR_IMG_CLASS
