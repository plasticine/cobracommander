from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from ..models.project import Project
from ..forms.NewProjectForm import NewProjectForm

def new(request):
    """
    Create a new Project
    """

    if request.method == 'POST':
        form = NewProjectForm(request.POST, request=request)
        if form.is_valid():
            project = form.save()
            return HttpResponseRedirect(reverse("project:show",
                          kwargs={'name_slug':project.name_slug}))
    else:
        form = NewProjectForm(request=request)

    return render_to_response('project/new.html', {
        'form':form
    }, context_instance=RequestContext(request))
