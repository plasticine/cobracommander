import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class Project(models.Model):
    """
    A project represents the top level interpretation of the codebase to be
    tested.

    A project may have one or many Targets.
    """

    targets             = models.ManyToManyField('build.Target', related_name="targets")

    created_datetime    = models.DateTimeField(blank=False, default=datetime.datetime.now)

    name                = models.CharField(blank=False, max_length=100)
    name_slug           = models.SlugField(blank=True, db_index=True, unique=True)
    url                 = models.CharField(blank=False, db_index=True, unique=True, max_length=255)
    github_url          = models.CharField(blank=True, unique=False, max_length=255)
    description         = models.TextField(blank=True)

    class Meta:
        app_label = 'project'

    def __unicode__(self):
        return u"%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('project:show', (), {
            'name_slug':self.name_slug
        })

    def save(self, *args, **kwargs):
        """
        set the name_slug from name on save
        """
        self.name_slug = u'%s' % slugify(self.name)
        super(Project, self).save(*args, **kwargs)
