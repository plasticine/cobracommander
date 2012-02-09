import hashlib
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Build

@receiver(post_save, sender=Build)
def set_uuid_for_build(sender, **kwargs):
    if kwargs.get('created') == True:
        obj = kwargs['instance']
        obj.uuid = hashlib.sha224("%s:%s:%s" % (obj.project, obj.target, obj.id)).hexdigest()[:7]
        obj.save()
