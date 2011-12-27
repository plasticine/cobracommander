from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from ..build.models import Build

class BuildsHandler(AnonymousBaseHandler):
    model = Build
    anonymous = 'AnonymousBuildsHandler'
    fields = (
        'uuid',
        'content',
        ('project', (
            'name',
            'name_slug',
        )),
        'created_datetime',
        'start_datetime',
        'end_datetime',
        'duration'
    )

    def read(self, request, title=None):
        base = Build.objects

        if title:
            return base.get(title=title)
        else:
            return base.all()
