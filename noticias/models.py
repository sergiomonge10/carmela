from django.db import models
from django.contrib.auth.models import User
from multimedia.models import Multimedia
from tinymce.models import HTMLField

# Create your models here.

class Noticia(models.Model):
        titulo = models.CharField(max_length=100)
        texto = HTMLField(blank=True, null=True)
        fecha = models.DateTimeField(auto_now_add=True)
        multimedia = models.ForeignKey(Multimedia, blank=True, null=True)
        usuario = models.ForeignKey(User)
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
