require [
  'vendor/jquery.1.7.1',
  'vendor/socket.io.0.6.1',
  'vendor/socket.io.channels',
], ->

  @module "cc.lib", ->
    class @SocketIO
      constructor: (url, options) ->
        @url = url
        @options = options

      connect: (autoReconnect=true, autoReconnectTimeout=2000) =>
        if not cc._socket
          if @.hasOwnProperty 'on_connecting'
            @on_connecting()
          cc._socket = new io.Socket(@url, @options)
          cc._socket.connect()

        cc._socket.on 'connect', @on_connect
        cc._socket.on 'message', (data) =>
          @on_message data
        cc._socket.on 'disconnect', (event) =>
          @websocket = null
          if autoReconnect
            window.setTimeout(
              (=> @connect(autoReconnect, autoReconnectTimeout)),
              autoReconnectTimeout
            )
          @on_disconnect event

      subscribe: (channel) =>
        cc._socket.send ['__subscribe__', channel]
        return cc._socket

      unsubscribe: (channel) =>
        cc._socket.send ['__unsubscribe__', channel]
        return cc._socket
