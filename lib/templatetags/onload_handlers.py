from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def set_onload_handler(context, name, *args, **kwargs):
  context['onload_handlers'][name] = kwargs
  return ''

@register.assignment_tag(takes_context=True)
def get_onload_handlers(context):
  return mark_safe(json.dumps(context['onload_handlers']))
