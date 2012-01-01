class App
  constructor: ->
    @version = 0.1
    @debug = on
    @onload_handlers = window.onload_handlers

  register_onload_handler: (handler_name, callback) =>
    if handler_name of @onload_handlers
      console.info "executing onload_handler for '#{handler_name}'" if cc.app.debug
      kwargs = @onload_handlers[handler_name]
      callback kwargs

require [
  'lib/module',
  'lib/SocketIO',
  'lib/Template',
  'vendor/jquery.1.7.1',
  'vendor/minpubsub'
], ->
  @module "cc", ->
    @app = new App()
    require [
      'app/build',
      'app/queue'
    ]
