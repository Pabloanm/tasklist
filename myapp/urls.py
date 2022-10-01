from django.urls import path #modulo "path"
from . import views #importo desde la "ruta actual(.)" las vistas"

#listado de urls que voy a exportar (similar al archivo mysyte\urls.py )
urlpatterns = [   
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
]