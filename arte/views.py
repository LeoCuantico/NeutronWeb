from django.shortcuts import render
from .models import Project

# Create your views here.

def arte(request):
    projects = Project.objects.all()
    return render(request,"arte/arte.html", {'projects' : projects})
