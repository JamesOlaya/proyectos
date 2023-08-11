from django.shortcuts import render
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
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
def tasks(request):
    tasks = list(Task.objects.values())
    return HttpResponse('<h1>tareas</h1>')