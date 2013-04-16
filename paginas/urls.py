from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('paginas.views',


	url(r'^tablaprimera/$','tabla1_view',name='view_tabla1'),

	url(r'^tablasegunda/$','tabla2_view',name='view_tabla2'),

	url(r'^calendario/$','partidos_view',name='view_partidos'),

	url(r'^contacto/$','contacto_view',name='view_contacto'),

	url(r'^nosotros/$','nosotros_view',name='view_nosotros'),

	)