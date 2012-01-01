def onload_handlers(request):
  """
  We need to set this here so that we have a "global" context varible to use
  later with our onload templatetags.
  """
  return {'onload_handlers':dict()}
