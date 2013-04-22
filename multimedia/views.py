from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from multimedia.models import CategoriaMultimedia,Multimedia,Patrocinador
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def galerias_view (request,page):
	galerias = CategoriaMultimedia.objects.filter(estado=True)
	ctx = {'galerias':galerias}
	return render_to_response('galerias.html',ctx,context_instance=RequestContext(request))

def galeria_view(request,id_categoria):
	imagenes = Multimedia.objects.filter(categoria_id=id_categoria)
	ctx = {'imagenes':imagenes}
	return render_to_response('imagenes.html',ctx,context_instance=RequestContext(request))


