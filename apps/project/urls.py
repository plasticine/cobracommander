from django.conf import settings
from django.conf.urls.defaults import *

import views as project

urlpatterns = patterns('',
    url(r'^$', project.index, name='index'),
    url(r'^project/new/$', project.new, name='new'),
    url(r'^project/(?P<name_slug>[0-9A-Za-z-]+)/$', project.show, name='show'),
)
