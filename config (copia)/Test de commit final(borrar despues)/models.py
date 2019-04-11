from django.db import models

# Create your models here.

class Libro(models.Model):
	autor = models.CharField(max_length=254)
	titulo = models.CharField(max_length=254)

	def __str__(self):
		return "Libro {}".format(self.titulo)

class Socio(models.Model):
	nombre = models.CharField(max_length=254)
	apellido = models.CharField(max_length=254)

	def __str__(self):
		return "Nombre {}".format(self.nombre)

class Prestamo(models.Model):
	libroId = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="libroId")
	socioId = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="socioId")
	fechaDevolucion = models.DateField(null=True, blank=True)
	fechaPrestamo = models.DateField()