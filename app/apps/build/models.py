from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from ..project.models import Project
from ..worker.tasks import exec_build
from ..worker.relay import BuildWebsocketRelay
import datetime
import multiprocessing


class Build(models.Model):
    """(Project description)"""
    
    STATE_CHOICES = (
        ("a", "pending",),
        ("b", "running",),
        ("c", "pass",),
        ("d", "fail",),
    )
    
    project = models.ForeignKey(Project)
    ref = models.CharField(blank=False, max_length=100, db_index=True)
    state = models.CharField(blank=True, max_length=1, default="a", choices=STATE_CHOICES)
    created_datetime = models.DateTimeField(blank=True, default=datetime.datetime.now)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" % (self.ref)
    
    @models.permalink
    def get_absolute_url(self):
        return ('build:show', (), {
            'build_ref':self.ref
        })

@receiver(post_save, sender=Build)
def trigger_build(sender, instance, **kwargs):
    async_build = exec_build.delay(build=instance)
    # running_builds = Build.objects.filter(state='b')
    # if not len(running_builds):
    #     build = instance
    #     queue = multiprocessing.Queue()
    #     buildProcess = multiprocessing.Process(
    #         target=BuildWebsocketRelay,
    #         name='buildwebsocketrelay',
    #         kwargs={
    #             'port':settings.BUILDRELAY_SOCKET_PORT,
    #             'path': build.project.get_absolute_url(),
    #             'queue':queue,
    #         }
    #     )
    #     buildProcess.start()
    #     # async_build = exec_build.delay(build=build)