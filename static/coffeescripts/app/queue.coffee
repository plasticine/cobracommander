require [
  'vendor/jquery.1.7.1',
  'vendor/underscore.1.2.3',
  'vendor/backbone.0.5.3',
  'templates/queue'
], (requirements...) ->

  Backbone = requirements[2]

  @module "cc.app.queue", ->

    class Build extends Backbone.Model

    class Builds extends Backbone.Collection
      model: Build

    # Represents a single view for a build instance in the build queue.
    class BuildView extends Backbone.View
      template:   cc._template_cache['build']
      events:     'click .cancel':   "_cancelBuild"

      initialize: (options) =>
        @element = $(@el)
        @render()

      render: =>
        @element.html @template.render(@model.attributes)

      _cancelBuild: (event) =>
        event.preventDefault()
        alert 'cancel clicked'


    # represents the "connecting", "disconnected", etc status messages in the
    # headers of each page.
    class QueueStatusView extends Backbone.View
      el:         "#build-queue-status",
      template:   cc._template_cache['build_status']

      initialize: (options) =>
        @element = $(@el)
        @initListeners()

      initListeners: =>
        subscribe "build_queue/on_connecting",    => @render status: "connecting"
        subscribe "build_queue/on_connect",       => @render status: "connected"
        subscribe "build_queue/on_disconnect",    => @render status: "disconnected"

      render: (context) =>
        @element.html @template.render(context)


    class QueueController extends cc.lib.SocketIO
      constructor: (options) ->
        super options.socketio_url, options.socketio_options
        @buildQueueEl = options.buildQueueEl
        @buildQueueStatusView = new QueueStatusView
        @builds = new Builds
        @connect()

      on_connecting: =>
        publish "build_queue/on_connecting"

      on_connect: =>
        publish "build_queue/on_connect"
        @subscribe 'build_queue'

      on_message: (message) =>
        message = JSON.parse message
        if message.length
          @buildQueueEl.empty()
          @builds.add message
          @builds.each (build) =>
            buildView = new BuildView(model: build)
            @buildQueueEl.append buildView.el

      on_disconnect: (event) =>
        publish "build_queue/on_disconnect"


    # onload handler for build_queue
    cc.app.register_onload_handler 'build_queue', (kwargs) ->
      new QueueController
        buildQueueEl: $('#build-queue'),
        socketio_url: "localhost",
        socketio_options:
          port: 9000
