import gevent
from collections import defaultdict
from werkzeug.wrappers import Response

from django_socketio import events
from django_socketio.channels import SocketIOChannelProxy

CLIENTS = {}


class SocketIO(object):
    """
    docstring for SocketIO
    """

    def __call__(self, request, method):
        context = {}
        socket = SocketIOChannelProxy(request.environ["socketio"])
        CLIENTS[socket.session.session_id] = (request, socket)

        try:
            if socket.on_connect():
                events.on_connect.send(request, socket, context)
            while True:
                message = socket.recv()
                if len(message) > 0:
                    print message
                    if message[0] == '__subscribe__' and len(message) == 2:
                        socket.subscribe(message[1])
                        events.on_subscribe.send(request, socket, context, message[1])
                    elif message[0] == '__unsubscribe__' and len(message) == 2:
                        socket.unsubscribe(message[1])
                        events.on_unsubscribe.send(request, socket, context, message[1])
                    else:
                        events.on_message.send(request, socket, context, message)
                else:
                    if not socket.connected():
                        events.on_disconnect.send(request, socket, context)
                        break
        except Exception, e:
            raise e

        return Response("")
