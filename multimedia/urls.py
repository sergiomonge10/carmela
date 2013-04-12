from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('multimedia.views',

	url(r'^galeria/page/(?P<page>.*)/$','galerias_view',name='view_galerias'),

	url(r'^galeria/(?P<id_categoria>.*)/$','galeria_view',name='view_galeria'),


	#url(r'^jugadoras/(?P<id_equipo>.*)/$','jugadoras_view',name='view_jugadoras'),

	#url(r'^jugadora/(?P<id_jugadora>.*)/$','jugadora_view',name='view_jugadora'),

	)