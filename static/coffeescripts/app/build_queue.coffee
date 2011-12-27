require [
  'vendor/jquery.1.7.1',
  'vendor/underscore.1.2.3',
  'vendor/backbone.0.5.3',
  'vendor/minpubsub',
  'templates/build_queue/build'
], (requirements...) ->

  Backbone = requirements[2]

  $ ->
    new BuildQueueController
      buildQueueEl: $('#build-queue'),
      url: "localhost",
      options:
        port: 9000


  class Build extends Backbone.Model


  class Builds extends Backbone.Collection
    model: Build


  class BuildView extends Backbone.View
    # Represents a single view for a build instance in the build queue.
    template:   cc._template_cache['build']
    events:     'click .cancel':   "cancelBuild"

    initialize: (options) =>
      @element = $(@el)
      @render()

    render: =>
      @element.html @template.render(@model.attributes)

    cancelBuild: (event) =>
      event.preventDefault()
      alert 'cancel clicked'


  class ActiveBuildView extends Backbone.View
    template:   cc._template_cache['active_build']
    events:     'click .cancel':   "cancelBuild"

    initialize: (options) =>
      @element = $(@el)
      @render()

    render: =>
      @element.html @template.render(@model.attributes)

    cancelBuild: (event) =>
      event.preventDefault()
      alert 'cancel clicked'


  class BuildQueueStatusView extends Backbone.View
    el:         "#build-queue-status",
    template:   cc._template_cache['build_status']

    initialize: (options) =>
      @element = $(@el)
      @initListeners()

    initListeners: =>
      subscribe "build_queue/on_connecting",  => @render status: "connecting"
      subscribe "build_queue/on_connect",     => @render status: "connected"
      subscribe "build_queue/disconnect",     => @render status: "disconnected"

    render: (context) =>
      @element.html @template.render(context)


  class BuildQueueController extends cc.lib.SocketIO
    constructor: (options) ->
      super options.url, options.options
      @buildQueueEl = options.buildQueueEl
      @buildQueueStatusView = new BuildQueueStatusView
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
          console.log build

