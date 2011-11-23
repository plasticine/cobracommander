from django.conf import settings
from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^project/(?P<name_slug>[0-9A-Za-z-]+)/(?P<refspec>[0-9A-Za-z-]+)/build/$',
          views.target.build_target, name='build_target'),
    url(r'^project/(?P<name_slug>[0-9A-Za-z-]+)/(?P<refspec>[0-9A-Za-z-]+)/build/(?P<id>[0-9]+)/$',
          views.build.show, name='show'),
)
