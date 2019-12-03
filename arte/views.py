from django.shortcuts import render
from .models import Project

# Create your views here.
# Vista para la pagina de /diseños, esto es basicamente la peticion que hace el servidor
# para llamar y mostrar el contenido de arte.html
def arte(request):
    projects = Project.objects.all()
    return render(request,"arte/arte.html", {'projects' : projects})
