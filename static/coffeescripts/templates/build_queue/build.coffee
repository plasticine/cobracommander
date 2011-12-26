new cc.lib.Template 'build', """
  <article>
    <a href="{{ url }}">project: {{ project }}</a>
    ({{ created_datetime }})
    <a href="#" class="cancel">cancel</a>
  </article>
"""

new cc.lib.Template 'active_build', """
  <article>
    Active! <a href="{{ url }}">project: {{ project }}</a>
    <a href="#" class="cancel">cancel</a>
  </article>
"""
