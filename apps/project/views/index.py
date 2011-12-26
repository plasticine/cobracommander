from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core import serializers

from ..models.project import Project

def index(request):
    """
    Dashboard view. Show all projects.
    """
    if request.is_ajax():
      return _backbone_endpoint(request)

    projects = Project.objects.all().prefetch_related('targets')
    return render_to_response('project/index.html', {
        "projects": projects,
    }, context_instance=RequestContext(request))


def _backbone_endpoint(request):
  json_serializer = serializers.get_serializer("json")()
  projects = Project.objects.all().prefetch_related('targets')
  json = json_serializer.serialize(projects, ensure_ascii=False)
  return HttpResponse(json, mimetype='application/json')
