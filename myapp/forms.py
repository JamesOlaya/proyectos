from django import forms 
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Task title', max_length=200)
    description = forms.CharField( label="Task description", widget=forms.Textarea)

    #CHOICES = (('Opcion1', 'Ocpcion1'), ('Opcion2', 'Ocpcion2'))
    #projecto_id = forms.ChoiceField(label="Project", widget=forms.Select(choices=CHOICES))
    
    CHOICES = Project.objects.all()
    project_id = forms.ModelChoiceField(label='Project', queryset=CHOICES)


class CreateNewProject(forms.Form):
    name = forms.CharField(label='Project name', max_length=200)
    