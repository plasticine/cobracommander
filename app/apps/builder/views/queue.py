import gevent
from collections import defaultdict
from django_socketio import events
from ..status.status_accessor import StatusAccessor
from ..builder import Builder

clients = set()
status_cache = None
builder_status = StatusAccessor(builder=Builder())

@events.on_subscribe(channel="build_queue")
def subscribe(request, socket, context, channel):
    """
    Websocket request for status updates.
    """
    # add websocket connection object to stack
    clients.add(socket)

    # always send the status to newly connecting clients
    if status_cache != None:
        message = status_cache
    else:
        message = builder_status.get_status()
    socket.send(message)


@events.on_finish(channel="build_queue")
def finish(request, socket, context):
    """
    clean up disconnecting client sockets
    """
    clients.remove(socket)


def update_build_status():
    while True:
        status_changed, status = builder_status.update()
        if status_changed:
            status_cache = status
            for client in clients:
                client.send(status)
        gevent.sleep(0.5)
gevent.spawn(update_build_status)
