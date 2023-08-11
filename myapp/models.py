from django.db import models

class Project(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    name = models.CharField(max_length=50, help_text='ingrese el nombre del proyecto')
    def __str__(self):
        return self.name

class Task(models.Model):
    '''
    Modelo que representan una tarea de un proyecto
    '''
    title = models.CharField(max_length=200, help_text='ingrese el título de la tarea.')
    descrption = models.TextField(help_text='ingrese la descripción de la tarea')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title + ' - ' + str(self.project.name)
    