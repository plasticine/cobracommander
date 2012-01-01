new cc.lib.Template 'build', """
  <article class="{{ status }}">
    <header>
      <h5>
        <a href="{{ build.absolute_url }}">
          {{ target.project }}
          <code>{{ target.refspec }}</code>
        </a>
      </h5>
      <a href="#" class="cancel">cancel</a>
    </header>
    <dl class="details">
      <dt>created:</dt>
      <dd>{{ build.created_datetime }}</dd>
      <dt>build uuid:</dt>
      <dd>{{ build.uuid }}</dd>
    </dl>
  </article>
"""

new cc.lib.Template 'build_status', """
  {{ status }}
"""
