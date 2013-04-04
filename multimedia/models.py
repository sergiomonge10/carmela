from django.db import models

# Create your models here.

class Patrocinador(models.Model):
	nombre = models.CharField(max_length=50)
	multimedia = models.ForeignKey("Multimedia")
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			super(Patrocinador, self).delete()
			return true

class CategoriaMultimedia(models.Model):

	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)
	padre = models.ForeignKey("self",blank=True,null=True)


	def __unicode__(self):
		return self.nombre

	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = True
			super(Multimedia, self).delete()
			return true
	

class Multimedia(models.Model):

		
        referencia = models.CharField(max_length=100)
        nombre = models.CharField(max_length=50)
        tipo = models.ForeignKey("TipoMultimedia")
        estado = models.BooleanField(default=True)
        categoria = models.ForeignKey("CategoriaMultimedia", blank=True, null=True)

        def __unicode__(self):
                return self.referencia

		def delete(self):
			if self.estado == False:
				return false
			else:
				self.estado = True
				super(Multimedia, self).delete()
				return true


class TipoMultimedia(models.Model):
	nombre = models.CharField(max_length=45)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

	def delete(self):
		if self.estado == False:
			return false
		else:
			self.estado = False
			super(TipoMultimedia, self).delete()
			return true

