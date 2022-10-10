from http.client import HTTPResponse
from django.shortcuts import render
from blog.models import Autor, Libro, Editorial
from django.http import HttpResponse
# Create your views here.

def mostrar_inicio(request):
    return render(request, "blog/inicio.html")

    
def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "blog/formulario.html")

    autor = Autor(nombre=request.POST["nombre"], apellido=request.POST["apellido"])
    autor.save()
    return render(request, "blog/inicio.html")

def procesar_formulario_libro(request):
    if request.method != "POST":
        return render(request, "blog/formulario-libro.html")

    libro = Libro(titulo=request.POST["titulo"], genero=request.POST["genero"], publicacion=request.POST["publicacion"] )
    libro.save()
    return render(request, "blog/inicio.html")

def procesar_formulario_editorial(request):
    if request.method != "POST":
        return render(request, "blog/formulario-editorial.html")

    editorial = Editorial(nombre=request.POST["nombre"])
    editorial.save()
    return render(request, "blog/inicio.html")

def busqueda(request):
    return render(request, "blog/busqueda.html")

def buscar(request):

    if not request.GET["nombre"]:
         return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        autores = Autor.objects.filter(nombre=nombre_a_buscar)


        contexto = {
            "nombre": nombre_a_buscar,
            "autores_encontrados": autores
        }
        
        return render(request, "blog/resultado_busqueda.html", contexto)