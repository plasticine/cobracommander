from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from ..models.project import Project

def index(request):
    """
    Dashboard view. Show all projects.
    """

    return render_to_response('project/index.html', {
        "projects": Project.objects.all(),
    }, context_instance=RequestContext(request))
