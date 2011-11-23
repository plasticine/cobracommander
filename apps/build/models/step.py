import datetime

from django.db import models
from django.core.urlresolvers import reverse

from .build import Build

class Step(models.Model):
    """
    Step represets a single command read from the snakefile from the Build
    the Step belongs to.

    Stores meta information about the execution of the step and its state.
    """

    STATE_CHOICES = (
        ("a", "pending",),
        ("b", "running",),
        ("c", "pass",),
        ("d", "fail",),
    )

    TYPE_CHOICES = (
        ("a", "setup",),
        ("b", "build",),
        ("c", "teardown",)
    )

    build               = models.ForeignKey(Build)

    created_datetime    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    start_datetime      = models.DateTimeField(blank=True, null=True)
    end_datetime        = models.DateTimeField(blank=True, null=True)

    uuid                = models.CharField(blank=True, max_length=255)
    type                = models.CharField(blank=True, max_length=1, default="b", choices=TYPE_CHOICES)
    state               = models.CharField(blank=True, max_length=1, default="a", choices=STATE_CHOICES)
    command             = models.CharField(blank=False, max_length=255)
    log                 = models.TextField(blank=True)

    class Meta:
        app_label = 'build'
        ordering = ['created_datetime']

    def __unicode__(self):
        return u"%s: %s" % (self.build, self.command)

