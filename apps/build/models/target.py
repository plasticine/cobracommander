import datetime

from django.db import models
from django.core.urlresolvers import reverse

from .build import Build


class Target(models.Model):
    """
    A Target provides a link between a Project and refspec in the Project codebase.

    Targets are used to as things to build against. By default all projects will
    have a minimum of one build target - `master`

    A Target will have between zero and many Builds that have been run with it
    as their target.
    """

    project                 = models.ForeignKey('project.Project')
    builds                  = models.ManyToManyField(Build, blank=True, null=True)

    created_datetime        = models.DateTimeField(blank=False, default=datetime.datetime.now)
    refspec                 = models.CharField(blank=False, max_length=128)

    class Meta:
        app_label = 'build'

    def __unicode__(self):
        return u"%s" % self.refspec

    def most_recent_build(self):
        return self.builds.all()[:1]

