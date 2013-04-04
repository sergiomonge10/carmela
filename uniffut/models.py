from django.db import models
from django.contrib.auth.models import User
from multimedia.models import Multimedia
from tinymce.models import HTMLField

# Create your models here.

class Bitacora(models.Model):
	accion = models.CharField(max_length=50)
	tabla = models.CharField(max_length=100)
	fecha = models.DateTimeField(auto_now_add=True)
	movimiento = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.movimiento

        def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			super(Bitacora, self).delete()
			return true



class Division(models.Model):
	nombre = models.CharField(max_length=50)
	torneo = models.ForeignKey("Torneo")
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre


	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			super(Division, self).delete()
			return true


class Torneo(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			super(Torneo, self).delete()
			return true



class Equipo(models.Model):
	nombre = models.CharField(max_length=50)
	division = models.ForeignKey("Division")
	descripcion = HTMLField(blank=True, null=True)
	multimedia = models.ForeignKey(Multimedia, blank=True, null=True)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

	def delete(self):
		if self.estado == False:
			return FALSE
		else:
			self.estado = False
			super(Equipo, self).delete()
			return TRUE



class Jugador(models.Model):
	nid = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	apellido1 = models.CharField(max_length=50)
	apellido2 = models.CharField(max_length=50)
	nacimiento = models.DateField()
	posicion = models.CharField(max_length=50)
	estatura = models.PositiveIntegerField()
	pais = models.CharField(max_length=50)
	capitan = models.BooleanField()
	equipo = models.ForeignKey("Equipo")
	multimedia = models.ForeignKey(Multimedia, blank=True, null=True)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			super(Jugador, self).delete()
			return true
