from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('noticias.views',

	url(r'^noticias/page/(?P<page>.*)/$','noticias_view',name='view_noticias'),

	url(r'^noticia/(?P<id_noticia>.*)/$','noticia_view',name='view_noticia'),

	#url(r'^jugadoras/(?P<id_equipo>.*)/$','jugadoras_view',name='view_jugadoras'),

	#url(r'^jugadora/(?P<id_jugadora>.*)/$','jugadora_view',name='view_jugadora'),

	)