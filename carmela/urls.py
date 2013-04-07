from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carmela.views.home', name='home'),
    # url(r'^carmela/', include('carmela.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^',include('uniffut.urls')),
    url(r'^',include('noticias.urls')),
    url(r'^',include('multimedia.urls')),
    url(r'^',include('paginas.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

    url(r'^tinymce/', include('tinymce.urls')),

     url(r'^admintools/', include('admin_tools.urls')),

      url(r'^admintools/', include('admin_tools.urls')),

    #(r'^photologue/', include('photologue.urls')),
)
