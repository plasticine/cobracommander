from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.doc import documentation_view

from .handlers import BuildsHandler

builds = Resource(handler=BuildsHandler)

urlpatterns = patterns('',
    url(r'^builds/$', builds),
    url(r'^builds/(?P<emitter_format>.+)/$', builds),
    url(r'^builds\.(?P<emitter_format>.+)', builds, name='blogposts'),

    # automated documentation
    url(r'^$', documentation_view),
)
