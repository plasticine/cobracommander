from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from ..models.project import Project
from apps.build.models.target import Target

def show(request, name_slug):
    """
    Show the Project and any Targets for the Project.
    """

    project = get_object_or_404(Project, name_slug=name_slug)
    targets = Target.objects.filter(project=project)
    return render_to_response('project/show.html', {
        "project": project,
        "targets": targets
    }, context_instance=RequestContext(request))
