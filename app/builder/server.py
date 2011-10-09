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
from .views import queue, build, socketio


class BuilderServer(WSGIWebsocketBase):
    """
    BuildRelay runs a WSGI server and listens for connections over websockets.
    """
    def __init__(self):
        self.logger = get_logger(__name__)
        self.url_map = Map([
            Rule('/', endpoint=root),
            Rule('/socket.io/<method>', endpoint=socketio.SocketIO()),
        ])
        super(BuilderServer, self).__init__()

def root(request):
    return Response('hello from the builder server')

if __name__ == '__main__':
    BuilderServer()
