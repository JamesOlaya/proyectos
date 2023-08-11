from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.

def index(request):
    return HttpResponse('<h1>Index page</h1>')

def hello( request, username ) :
    print(username)
    return HttpResponse("hello %s" % username)

def about( request ):
    return HttpResponse('<h1>about us</h1>')

def product (request):
    return HttpResponse('<h1>product</h1>')

def number(request, num):
    result = (num+100)*2
    return HttpResponse('<h1>el resultado de (%s +100 ) * 2 es %i</h1>' % (num,result))

#listando todos los proyectos
def projects(request, p_name):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    project = get_object_or_404(Project, name= p_name )
    return HttpResponse('<h1>proyecto %s</h1>' % project.name)
# listar una tarea
def tasks(request, id):
    #task = Task.objects.get(id = id )
    task = get_object_or_404(Task, id=id)
    return HttpResponse('<h1>tareas %s</h1>' % task.title)
# hacer las modificaciones necesarias para que busque un proyecto por el nombre
