require [
  'vendor/jquery.1.7.1',
  'vendor/underscore.1.2.3',
  'vendor/backbone.0.5.3'
], (requirements...) ->

  Backbone = requirements[2]

  @module "cc.app.build", ->

    class Build extends Backbone.Model

    class ConsoleLine extends Backbone.Model

    class ConsoleLines extends Backbone.Collection
      model: ConsoleLine

    class BuildController extends cc.lib.SocketIO
      constructor: (options) ->
        super options.socketio_url, options.socketio_options
        @buildUuid = options.build_uuid
        @buildConsoleEl = options.build_console_el
        @consoleLines = new ConsoleLines
        @connect()

      on_connecting: =>
        publish "build/on_connecting"

      on_connect: =>
        publish "build/on_connect"
        @subscribe "build_#{@buildUuid}_console"

      on_message: (message) =>
        message = JSON.parse message
        console.log message

      on_disconnect: (event) =>
        publish "build/on_disconnect"


    # onload handler for build_queue
    cc.app.register_onload_handler 'build', (kwargs) ->
      new BuildController
        build_uuid: kwargs.build_uuid,
        build_console_el: $('#console-output'),
        socketio_url: "localhost",
        socketio_options:
          port: 9000
