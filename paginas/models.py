from django.db import models
from tinymce.models import HTMLField
from uniffut.models import Equipo

# Create your models here.

class Pagina(models.Model):
        titulo = models.CharField(max_length=100)
        texto = HTMLField(blank=True, null=True)
        estado = models.BooleanField(default=True)

        def __unicode__(self):
                return self.titulo

	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			self.save()
			return true

	
class TablaPrimera(models.Model):
	equipo = models.ForeignKey(Equipo)
	juegos = models.IntegerField()
	GolesFavor = models.IntegerField()
	GolesContra = models.IntegerField()
	GolDiferencia = models.IntegerField()
	puntos = models.IntegerField()

	def __unicode__(self,):
		return self.equipo

	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			self.save()
			return true

	
class TablaSegunda(models.Model):
	equipo = models.ForeignKey(Equipo)
	juegos = models.IntegerField()
	GolesFavor = models.IntegerField()
	GolesContra = models.IntegerField()
	GolDiferencia = models.IntegerField()
	puntos = models.IntegerField()

	def __unicode__(self,):
		return self.equipo


	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			self.save()
			return true


class Partido(models.Model):
	equipoLocal = models.ForeignKey(Equipo,related_name='equipoLocal')
	equipoVisita = models.ForeignKey(Equipo,related_name='equipoVisita')
	fecha = models.DateTimeField()
	lugar = models.CharField(max_length=100)
	estadio = models.CharField(max_length=100)
	jornada = models.IntegerField()

	def __unicode__(self,):
		return self.lugar


	
		