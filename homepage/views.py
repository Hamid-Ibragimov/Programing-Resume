from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.

# def homepage_view(request,*args, **kwargs):
#     return render(request, "home/home.html", {})

def homepage_view(request,*args, **kwargs):
    queryset=Project.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "home/home.html", context)

# def project_menu_view(request, *args, **kwargs):
#     queryset=Project.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "home/home.html", context)

def test_view(request,*args, **kwargs):
    return render(request, "test.html", {})