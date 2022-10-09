from django.contrib import admin
from django.urls import path, include
from blog.views import (mostrar_inicio, procesar_formulario, busqueda, buscar)


urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario/", procesar_formulario, name="formulario"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
    ]