from django.contrib import admin
from django.urls import path
from Proyecto1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', vista_plantilla),
    #path('alumnos/', vista_listado_alumnos),
    path('alumnos/', vista_listado_alumnos2),
]
