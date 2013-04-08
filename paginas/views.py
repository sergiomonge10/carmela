from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from paginas.models import TablaPrimera,TablaSegunda,Partido

def tabla1_view(request):
	tabla = TablaPrimera.objects.order_by('-puntos','-GolDiferencia')
	ctx = {'tabla':tabla}
	return render_to_response('tablaprimera.html',ctx,context_instance=RequestContext(request))

def tabla2_view(request):
	tabla = TablaSegunda.objects.order_by('-puntos','-GolDiferencia')
	ctx = {'tabla':tabla}
	return render_to_response('tablasegunda.html',ctx,context_instance=RequestContext(request))

def partidos_view(request):
	partidos = Partido.objects.all().order_by('-jornada')
	ctx = {'partidos':partidos}
	return render_to_response('partidos.html',ctx,context_instance=RequestContext(request))
