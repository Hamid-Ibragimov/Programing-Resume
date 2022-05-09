from django.shortcuts import render,get_object_or_404
from .models import Project

# Create your views here.
def project_menu_view(request, *args, **kwargs):
    queryset=Project.objects.all()
    context = {
        "object_list" : queryset

    }
    return render(request, "project_menu.html", context)

def project_view(request,id, *args, **kwargs):
    obj = get_object_or_404(Project, id=id)
    context = {
        "obj": obj
    }
    return render(request, "project.html", context)
