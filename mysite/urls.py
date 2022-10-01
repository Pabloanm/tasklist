"""mysite URL Global Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from myapp.views import hello # Ejem 1: asi estoy importando solo la function "hello" de "views")
# from myapp import views #Ejem 2: asi estoy importando todas las functions de "views"
from django.urls import path, include #include sirve para incluir un bloque de urls que vienen de una app


#acá importo las rutas.
urlpatterns = [
    path('admin/', admin.site.urls), #modulo de django
    #path('', hello)  Ejem1: asi estoy llamando solo la function "hello" de "views")
    #path('', views.hello)  Ejem2: asi estoy llamando solo la function "hello" de "views")
    #path('about/', views.about)  Ejem3 nueva ruta "about" llama a la function "about" de "views")
    path ('', include('myapp.urls')) #Ejem 4('' ruta del localhost, todas las urls que vienen de myapp\urls.py)
    
]
