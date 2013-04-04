from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('uniffut.views',

	url(r'^$','index_view',name='view_index'),

	url(r'^equipos/$','equipos_view',name='view_equipos'),

	url(r'^equipo/(?P<id_equipo>.*)/$','equipo_view',name='view_equipo'),

	url(r'^jugadoras/(?P<id_equipo>.*)/$','jugadoras_view',name='view_jugadoras'),

	url(r'^jugadora/(?P<id_jugadora>.*)/$','jugadora_view',name='view_jugadora'),

	)