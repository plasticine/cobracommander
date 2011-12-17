from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import transaction
import requests
import hashlib

from ..models.target import Target
from ..models.build import Build
from apps.project.models import Project

@transaction.autocommit
def build_target(request, name_slug, refspec=None):
    """
    Trigger a build run on the given target and project.

    Adds the build details to the redis queue for minion to pick up and process.
    Creates a new Build instance and creates the relationship with the Target.

    If `refspec` is passed then the build was probably started by cobracommander.
    If it is not present it usually means that it was triggered by a GitHub
    post-commit hook.

    View needs to be autocommited as we are doing the POST to henchman in here
    that will kick off a DB query looking for out newly minted record when will
    not yet be there if we are using transactions on_success.
    """
    if request.method == 'POST':
      project = get_object_or_404(Project, name_slug=name_slug)

      if not refspec:
        import simplejson as json
        github_postcommit_data = json.loads(request.POST)
        refspec = github_postcommit_data['ref'].split('/')[-1]

      target = get_object_or_404(Target, project=project, refspec=refspec)
      uuid = hashlib.sha224("%s%s" % (project, target)).hexdigest()[:7]
      build = Build(project=project, uuid=uuid)
      build.save()
      target.builds.add(build)
      target.save()

      # push the build id onto the build queue by making a POST request
      # to Henchman
      post_data = { 'id': build.id }
      request = requests.post('http://localhost:9000/builds/new', data=post_data)

      return HttpResponseRedirect(build.get_absolute_url())
    raise Http404
