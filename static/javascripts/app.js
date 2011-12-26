(function() {
  require(['lib/module', 'lib/Template', 'app/build_queue'], function() {
    return this.module("cc", function() {
      return cc.version = "0.1";
    });
  });
}).call(this);
