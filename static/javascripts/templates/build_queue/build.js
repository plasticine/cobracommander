(function() {
  new cc.lib.Template('build', "<article>\n  <a href=\"{{ url }}\">project: {{ project }}</a>\n  ({{ created_datetime }})\n  <a href=\"#\" class=\"cancel\">cancel</a>\n</article>");
  new cc.lib.Template('active_build', "<article>\n  Active! <a href=\"{{ url }}\">project: {{ project }}</a>\n  <a href=\"#\" class=\"cancel\">cancel</a>\n</article>");
}).call(this);
