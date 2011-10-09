import re, urlparse
import gevent
from django.utils import simplejson
from collections import defaultdict
from werkzeug.utils import redirect
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound

from .utils import get_logger
from .utils.wsgi import WSGIWebsocketBase

from .builder import Builder
from .views import queue, build

class BuildRelay(WSGIWebsocketBase):
    """
    BuildRelay runs a WSGI server and listens for connections over websockets.
    """
    def __init__(self):
        self.logger = get_logger(__name__)
        self.builder = Builder()
        self.url_map = Map([
            Rule('/builder/status', endpoint=status.BuilderStatus(builder=self.builder)),
            Rule('/builder/build/<build_id>/console', endpoint=build.BuildConsole()),
            Rule('/builder/build/<build_id>/stop', endpoint=build.stop)
        ])
        super(BuildRelay, self).__init__()
