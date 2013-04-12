from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from noticias.models import Noticia
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def noticias_view(request,page):
	listnoticias = Noticia.objects.order_by('-fecha')
	paginator = Paginator(listnoticias,3)
	try:
		page = int(page)
	except:
		page = 1
	try:
		noticias = paginator.page(page)
	except (EmptyPage,InvalidPage):
		noticias = paginator.page(paginator.num_pages)
	ctx = {'noticias':noticias}
	return render_to_response('noticias.html',ctx,context_instance=RequestContext(request))

def noticia_view(request,id_noticia):
	noticia = Noticia.objects.get(id=id_noticia)
	ctx = {'noticia':noticia}	
	return render_to_response('noticia.html',ctx,context_instance=RequestContext(request))

def ultimasNoticias_view(request):
	noticias = Noticia.objects.order_by('-fecha')[:5]
	ctx = {'noticias':noticias}
	return render_to_response('equipos.html',ctx,context_instance=RequestContext(request))