from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
	
	context = {}
	context["todos_los_prestamos"] = Prestamo.objects.filter(fechaDevolucion=None)

	return render(request, "index.html", context)

def socioEspecifico(request, socio_id):
	
	context = {}
	context["todos_los_socios"] = Prestamo.objects.filter(socioId=socio_id)

	return render(request, "socios.html", context)

	#--------------------------------------------------------------------------------
	#HACER QUE MUESTRE LA CANTIDAD DE LIBROS QUE NO SE DEVOLVIERON (todos los none)
	#--------------------------------------------------------------------------------