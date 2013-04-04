from django.contrib import admin
from multimedia.models import CategoriaMultimedia,Patrocinador,Multimedia,TipoMultimedia

admin.site.register(Patrocinador)
admin.site.register(Multimedia)
admin.site.register(TipoMultimedia)
admin.site.register(CategoriaMultimedia)