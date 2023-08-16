from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask,CreateNewProject


# Create your views here.

def index(request):
    title = 'Django Projects!!'
    return render(request,'index.html',{
        'title': title  
    })

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
    #return JsonResponse(projects, safe=False)
    #project = get_object_or_404(list(Project.objects.values()), name= p_name )
    #return JsonResponse(project.name, safe=False)
    title = 'Welcome to Django Projects'
    return render(request, 'Projects/projects.html',{
        'title': title,
        'projects': projects
    })
# listar una tarea
def tasks(request):
    #task = Task.objects.get(id = id )
    #task = get_object_or_404(Task, id=id)
    #return render('<h1>tareas %s</h1>' % task.title)
    tasks = Task.objects.all()
    return render(request, 'Tasks/tasks.html',{
        'tasks': tasks, 
    })
# hacer las modificaciones necesarias para que busque un proyecto por el nombre

def create_task(request):
    if request.method == 'GET':
        return render(request, 'Tasks/create_task.html',{
            'form': CreateNewTask()
        })
    else:
        title = request.POST['title']
        descrption = request.POST['description']
        project_id = request.POST['project_id']
        Task.objects.create(title =title, descrption=descrption, project_id=project_id)
        return redirect('/tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request,'Projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        name = request.POST['name']
        Project.objects.create(name = name)
        return redirect('/projects')
def tasks_project(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.all().filter(project_id=project_id)
    return render(request, 'Tasks/projects.thml',{
        'project': project.name,
        'tasks': tasks
    })


# gestionar los datos de las bibliotecsa de una universidad, de cada biblioteca interasa el nombre de la biblioteca y su ubicacion en la universidad, cada biblioteca tiene una coleccion de libros en donde para cada libro interesa saber el nombre, el isbn, autor y el estado, que ele stado puede ser en sala o prestado, interesa poder agregar nuevos libros para cada colecion de cada biblioteca.

# el modelo de la abse de datos
# las historias de usuario segun el enunciado
#mañana se codifica todo