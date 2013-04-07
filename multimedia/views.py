from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from multimedia.models import CategoriaMultimedia,Multimedia,Patrocinador
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def galerias_view (request,page):
	listgalerias = CategoriaMultimedia.objects.filter()
	paginator = Paginator(listgalerias,5)
	try:
		page = int(page)
	except:
		page = 1
	try:
		galerias = paginator.page(page)
	except (EmptyPage,InvalidPage):
		gelerias = paginator.page(paginator.num_pages)
	ctx = {'galerias':galerias}
	return render_to_response('galerias.html',ctx,context_instance=RequestContext(request))

def galeria_view(request,id_categoria):
	imagenes = Multimedia.objects.filter(categoria_id=id_categoria)
	ctx = {'imagenes':imagenes}
	return render_to_response('imagenes.html',ctx,context_instance=RequestContext(request))

def patrocinadores_view(request):
	patrocinadores = Patrocinador.objects.filter()
	ctx = {'patrocinadores':patrocinadores}
	return render_to_response('base.html',ctx,context_instance=RequestContext(request))
