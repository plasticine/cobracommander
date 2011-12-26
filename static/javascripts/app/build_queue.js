(function() {
  var __slice = Array.prototype.slice, __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
  require(['vendor/jquery.1.7.1', 'vendor/underscore.1.2.3', 'vendor/backbone.0.5.3', 'vendor/minpubsub', 'templates/build_queue/build'], function() {
    var ActiveBuildView, Backbone, Build, BuildQueueController, BuildView, Builds, options;
    options = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
    Backbone = options[2];
    Build = (function() {
      __extends(Build, Backbone.Model);
      function Build() {
        Build.__super__.constructor.apply(this, arguments);
      }
      Build.prototype.defaults = {
        project: "Some Project",
        active: false,
        url: "/foo/bar",
        created_datetime: new Date,
        start_datetime: null,
        end_datetime: null,
        duration: null
      };
      return Build;
    })();
    Builds = (function() {
      __extends(Builds, Backbone.Collection);
      function Builds() {
        Builds.__super__.constructor.apply(this, arguments);
      }
      Builds.prototype.model = Build;
      return Builds;
    })();
    BuildView = (function() {
      __extends(BuildView, Backbone.View);
      function BuildView() {
        this.cancelBuild = __bind(this.cancelBuild, this);
        this.render = __bind(this.render, this);
        this.initialize = __bind(this.initialize, this);
        BuildView.__super__.constructor.apply(this, arguments);
      }
      "Represents a single view for a build instance in the build queue.";
      BuildView.prototype.template = cc._template_cache['build'];
      BuildView.prototype.events = {
        'click .cancel': "cancelBuild"
      };
      BuildView.prototype.initialize = function(options) {
        this.element = $(this.el);
        return this.render();
      };
      BuildView.prototype.render = function() {
        return this.element.html(this.template.render(this.model.attributes));
      };
      BuildView.prototype.cancelBuild = function(event) {
        event.preventDefault();
        return alert('cancel clicked');
      };
      return BuildView;
    })();
    ActiveBuildView = (function() {
      __extends(ActiveBuildView, Backbone.View);
      function ActiveBuildView() {
        this.cancelBuild = __bind(this.cancelBuild, this);
        this.render = __bind(this.render, this);
        this.initialize = __bind(this.initialize, this);
        ActiveBuildView.__super__.constructor.apply(this, arguments);
      }
      "Represents a view for the active build instance in the build queue.";
      ActiveBuildView.prototype.template = cc._template_cache['active_build'];
      ActiveBuildView.prototype.events = {
        'click .cancel': "cancelBuild"
      };
      ActiveBuildView.prototype.initialize = function(options) {
        this.element = $(this.el);
        return this.render();
      };
      ActiveBuildView.prototype.render = function() {
        return this.element.html(this.template.render(this.model.attributes));
      };
      ActiveBuildView.prototype.cancelBuild = function(event) {
        event.preventDefault();
        return alert('cancel clicked');
      };
      return ActiveBuildView;
    })();
    BuildQueueController = (function() {
      function BuildQueueController(options) {
        this.initBuildView = __bind(this.initBuildView, this);
        this.initBuildViews = __bind(this.initBuildViews, this);
        this.loadBuilds = __bind(this.loadBuilds, this);        this.buildQueueEl = options.el;
        this.loadBuilds();
        this.initBuildViews();
      }
      BuildQueueController.prototype.loadBuilds = function() {
        this.builds = new Builds;
        $.getJSON('/', function(projects) {
          return console.log(projects);
        });
        return this.builds.add([
          {
            project: "foo"
          }, {
            project: "bar"
          }, {
            project: "baz"
          }
        ]);
      };
      BuildQueueController.prototype.initBuildViews = function() {
        return this.builds.each(__bind(function(build) {
          return this.initBuildView(build);
        }, this));
      };
      BuildQueueController.prototype.initBuildView = function(build) {
        var buildView;
        buildView = new BuildView({
          model: build
        });
        return this.buildQueueEl.append(buildView.el);
      };
      return BuildQueueController;
    })();
    return $(function() {
      return new BuildQueueController({
        el: $('#build-queue')
      });
    });
  });
}).call(this);
