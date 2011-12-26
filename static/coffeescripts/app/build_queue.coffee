require [
  'vendor/jquery.1.7.1',
  'vendor/underscore.1.2.3',
  'vendor/backbone.0.5.3',
  'vendor/minpubsub',
  'templates/build_queue/build'
], (options...) ->

  Backbone = options[2]

  class Build extends Backbone.Model
    defaults:
      project:                "Some Project"
      active:                 false
      url:                    "/foo/bar"
      created_datetime:       new Date
      start_datetime:         null
      end_datetime:           null
      duration:               null


  class Builds extends Backbone.Collection
    model: Build


  class BuildView extends Backbone.View
    """
    Represents a single view for a build instance in the build queue.
    """
    template: cc._template_cache['build']
    events:
      'click .cancel':   "cancelBuild"

    initialize: (options) =>
      @element = $(@el)
      @render()

    render: =>
      @element.html @template.render(@model.attributes)

    cancelBuild: (event) =>
      event.preventDefault()
      alert 'cancel clicked'


  class ActiveBuildView extends Backbone.View
    """
    Represents a view for the active build instance in the build queue.
    """
    template: cc._template_cache['active_build']
    events:
      'click .cancel':   "cancelBuild"

    initialize: (options) =>
      @element = $(@el)
      @render()

    render: =>
      @element.html @template.render(@model.attributes)

    cancelBuild: (event) =>
      event.preventDefault()
      alert 'cancel clicked'


  class BuildQueueController
    constructor: (options) ->
      @buildQueueEl = options.el
      @loadBuilds()
      @initBuildViews()

    loadBuilds: =>
      @builds = new Builds

      $.getJSON '/', (projects) ->
        console.log projects

      @builds.add [
        {project: "foo"}
        {project: "bar"}
        {project: "baz"}
      ]

    initBuildViews: =>
      @builds.each (build) =>
        @initBuildView build

    initBuildView: (build) =>
      buildView = new BuildView(model: build)
      @buildQueueEl.append buildView.el

  $ ->
    new BuildQueueController el: $('#build-queue')

