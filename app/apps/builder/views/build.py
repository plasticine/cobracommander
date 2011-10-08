import gevent
import redis
from collections import defaultdict
from django.http import HttpResponse
from django.conf import settings
from django.utils import simplejson
from django_socketio import events

redis = redis.Redis(**settings.REDIS_DATABASE)
clients = defaultdict(set)
channel = r"^build_[0-9]+_output"
console_buffer = defaultdict(list)
build_updater = defaultdict(list)

@events.on_subscribe(channel=channel)
def subscribe(request, socket, context, channel):

    # create a build updater process for this build if it does not exist.
    if not channel in build_updater:
        build_updater[channel] = gevent.spawn(update_build_log, channel=channel)

    # add websocket connection object to stack
    clients[channel].add(socket)

    # always send the status to newly connecting clients
    if len(console_buffer[channel]):
        socket.send(simplejson.dumps(console_buffer[channel]))


@events.on_finish(channel=channel)
def finish(request, socket, context):
    """ clean up disconnecting client sockets """
    clients[channel].remove(websocket)

    # clean up internal pointers if there are no clients.
    if len(clients[channel]) == 0:
        del clients[channel]
        del console_buffer[channel]
        build_updater[channel].kill()
        del build_updater[channel]


def update_build_log(channel):
    redis_key = channel
    last_index = 0
    console_length = 0
    while True:
        console_length = redis.llen(redis_key)
        if console_length:
            lines = redis.lrange(redis_key, last_index, console_length)
            lines = filter(None, lines)
            if lines:
                last_index = console_length
                if type(lines) == type(list()):
                    lines = map(simplejson.loads, lines)
                    console_buffer[channel] += lines
                    for line in lines:
                        for client in clients[channel]:
                            client.send(simplejson.dumps(line))
        gevent.sleep(0.05)
