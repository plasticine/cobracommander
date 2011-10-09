@module "cc", ->
  @module "lib", ->
    class @SocketIOWrapper
      constructor: (url, options) ->
        @__name__ = "[cc.lib.SocketIOWrapper]"
        @url = url
        @options = options

      connect: (autoReconnect=true, autoReconnectTimeout=2000) =>
        if cc.socket == null
          if @.hasOwnProperty('on_connecting')
            @on_connecting()
          if cc.debug
            console.log @__name__, 'connect', @url, @options
          cc.socket = new io.Socket(@url, @options)
          cc.socket.connect()
        cc.socket.on('connect', @on_connect)
        cc.socket.on('message', (data) =>
          @on_message(data)
        )
        cc.socket.on('disconnect', (event) =>
          @websocket = null
          if autoReconnect
            window.setTimeout(
              (=> @connect(autoReconnect, autoReconnectTimeout)),
              autoReconnectTimeout
            )
          @on_disconnect(event)
        )

      subscribe: (channel) =>
        if cc.debug
          console.log @__name__, '__subscribe__', channel
        cc.socket.send(['__subscribe__', channel])
        return cc.socket

      unsubscribe: (channel) =>
        if cc.debug
          console.log @__name__, '__subscribe__', channel
        cc.socket.send(['__unsubscribe__', channel])
        return cc.socket
