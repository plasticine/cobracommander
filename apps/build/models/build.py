import datetime

from django.db import models
from django.core.urlresolvers import reverse

class Build(models.Model):
    """
    Represents a single test run of a Project.

    A Build is characterised by the Project and the commit ref that is to be tested.
    A Build contains one or more Step references that represent the individual
    commands that need to be run to execute the build - as read from the Project
    snakefile.
    """

    project                 = models.ForeignKey('project.Project')

    created_datetime        = models.DateTimeField(blank=False, default=datetime.datetime.now)
    start_datetime          = models.DateTimeField(blank=True, null=True)
    end_datetime            = models.DateTimeField(blank=True, null=True)

    duration                = models.BigIntegerField(blank=True, null=True)
    log                     = models.TextField(blank=True)
    git_refspec             = models.CharField(blank=True, max_length=42)
    git_author_name         = models.CharField(blank=True, max_length=128)
    git_author_email        = models.CharField(blank=True, max_length=128)
    git_message             = models.TextField(blank=True)
    git_commit_datetime     = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'build'
        ordering = ['-created_datetime']

    def __unicode__(self):
        return u"%s" % (self.id)

    @models.permalink
    def get_absolute_url(self):
        return ('build:show', (), {
            'id':self.id,
            'name_slug':self.project.name_slug,
            'refspec':self.target_set.all()[0].refspec
        })

