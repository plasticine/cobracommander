from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
import requests

from ..models.target import Target
from ..models.build import Build
from apps.project.models import Project

def build_target(request, name_slug, refspec):
    """
    Trigger a build run on the given target and project.

    Adds the build details to the redis queue for minion to pick up and process.
    Creates a new Build instance and creates the relationship with the Target.
    """

    project = get_object_or_404(Project, name_slug=name_slug)
    target = get_object_or_404(Target, project=project, refspec=refspec)

    if request.method == 'POST':
      build = Build(project=project)
      build.save()
      target.builds.add(build)
      target.save()

      # push the build id onto the build queue by making a POST request
      # to Henchman


      return HttpResponseRedirect(build.get_absolute_url())

    raise Http404
