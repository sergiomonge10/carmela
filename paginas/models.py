from django.db import models
from tinymce.models import HTMLField

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
			super(Pagina, self).delete()
			return true
	
