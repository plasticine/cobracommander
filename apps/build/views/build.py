from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from ..models.build import Build
from ..models.step import Step
from apps.project.models import Project


def show(request, name_slug, refspec, id):
    """
    Show the details of a build.
    """
    project = get_object_or_404(Project, name_slug=name_slug)
    build = get_object_or_404(Build, id=id)

    return render_to_response('build/show.html', {
        "project":project,
        "build": build,
    }, context_instance=RequestContext(request))
