from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def cargarInicio(request):
	return render(request, 'aplicacion/index.html')

def cargarFormulario(request):
	return render(request, 'aplicacion/formulario-usuario.html')

def seguirUsuario(request):
	return render(request, 'aplicacion/seguir-usuario.html')	