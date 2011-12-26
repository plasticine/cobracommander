(function() {
  var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
  require(['vendor/hogan'], function(hogan) {
    return this.module("cc", function() {
      this._template_cache = {};
      return this.module("lib", function() {
        return this.Template = (function() {
          function Template(name, template) {
            this.render = __bind(this.render, this);            cc._template_cache[name] = hogan.compile(template);
          }
          Template.prototype.render = function(context) {
            return cc._template_cache[name].render(context);
          };
          return Template;
        })();
      });
    });
  });
}).call(this);
