from django.contrib import admin
from .models import Project, Task #importo el modelo Project, Task en el panel Admin

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)