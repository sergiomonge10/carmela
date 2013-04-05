from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('paginas.views',


	url(r'^tabla/$','tabla_view',name='view_tabla'),

	)