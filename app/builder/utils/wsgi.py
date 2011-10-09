from werkzeug.utils import redirect
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound

from geventwebsocket.handler import WebSocketHandler
from socketio.handler import SocketIOHandler
from socketio.server import SocketIOServer

from gevent import pywsgi
from collections import defaultdict
from django.conf import settings


class WSGIWebsocketBase(object):
    """
    Setup up basic functions afor WSGI app; dispatch of request response,
    etc...
    """
    def __init__(self):
        self.serve()

    def serve(self):
        """ start server, listen for incoming requests """
        connection = (settings.DJANGO_SOCKETIO_HOST,
            settings.DJANGO_SOCKETIO_PORT)
        self.logger.info("Serving on http://%s:%s", connection[0], connection[1])
        self.server = SocketIOServer(connection, self.wsgi_app,
            handler_class=SocketIOHandler, resource="socket.io", policy_server=False)
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            raise

    def wsgi_app(self, environ, start_response):
        """ Set up the response cycle """
        response = self.dispatch(Request(environ))
        return response(environ, start_response)

    def dispatch(self, request):
        """
        dispatch the matched request to the view function based on on_*viewname*
        pattern. Will pass websocket object to view if it is present in the
        request environment
        """
        adapter = self.url_map.bind_to_environ(request.environ)
        endpoint, values = adapter.match()
        return endpoint(request, **values)
