require ['vendor/hogan'], (hogan) ->
  @module "cc", ->
    @_template_cache = {}
    @module "lib", ->
      class @Template
        constructor: (name, template) ->
          cc._template_cache[name] = hogan.compile template

        render: (context) =>
          return cc._template_cache[name].render context

