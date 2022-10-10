from django.contrib import admin
from django.urls import path, include
from blog.views import (mostrar_inicio, procesar_formulario, procesar_formulario_libro, procesar_formulario_editorial, busqueda, buscar)


urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario/", procesar_formulario, name="formulario"),
    path("formulario-libro/", procesar_formulario_libro, name="formulario_libro"),
    path("formulario-editorial/", procesar_formulario_editorial, name="formulario_editorial"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
    ]