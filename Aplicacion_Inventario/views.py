from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "Aplicacion_Inventario/index.html")

def notebooks(request):
    contexto = {'notebooks': Notebook.objects.all()}
    return render(request, 'Aplicacion_Inventario/notebooks.html', contexto)

def campanias(request):
    contexto = {'campanias': Campania.objects.order_by('id')}
    return render(request, 'Aplicacion_Inventario/campanias.html', contexto)

def perifericos(request):
    contexto = {
        'mouses': Mouse.objects.order_by('id'),
        'headsets': Headset.objects.order_by('id')
    }
    return render(request, 'Aplicacion_Inventario/perifericos.html', contexto)

def personas(request):
    contexto = {'personas': Persona.objects.all()}
    return render(request, 'Aplicacion_Inventario/personas.html', contexto)

def computadoras_escritorio(request):
    contexto = {'computadoras': Computadora.objects.all()}
    return render(request, 'Aplicacion_Inventario/computadoras_escritorio.html', contexto)

def agregar_notebook(request):
    contexto = {'notebooks': Notebook.objects.all()}
    return render(request, 'Aplicacion_Inventario/agregar_notebook.html', contexto)

def eliminar_notebook(request):
    contexto = {'notebooks': Notebook.objects.all()}
    return render(request, 'Aplicacion_Inventario/eliminar_notebook.html', contexto)

def actualizar_notebook(request):
    contexto = {'notebooks': Notebook.objects.all()}
    return render(request, 'Aplicacion_Inventario/actualizar_notebook.html', contexto)   