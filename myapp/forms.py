from django import forms #form
#from .models import Project


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    #traigo el id del proyecto    
    #projects = Project.objects.all() #mando el listado de proyectos
    CHOICES = (
      (1, 'Orange'),
      (2, 'Mango'),
      (3, 'Strawberries'),
      (4, 'Grapes'),
      
    )
    project=forms.ChoiceField(choices=CHOICES)

    

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyect", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))