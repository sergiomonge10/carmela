from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from uniffut.models import Equipo,Jugador


def index_view(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def equipos_view(request):
	equipos = Equipo.objects.filter()
	ctx = {'equipos':equipos}
	return render_to_response('equipos.html',ctx,context_instance=RequestContext(request))

def equipo_view(request,id_equipo):
	equipo = Equipo.objects.get(id=id_equipo)
	ctx = {'equipo':equipo}
	return render_to_response('equipo.html',ctx,context_instance=RequestContext(request))

def jugadoras_view(request,id_equipo):
	jugadoras = Jugador.objects.filter(equipo_id=id_equipo)
	ctx = {'jugadoras':jugadoras}
	return render_to_response('jugadoras.html',ctx,context_instance=RequestContext(request))


def jugadora_view(request,id_jugadora):
	jugadora = Jugador.objects.get(id=id_jugadora)
	ctx = {'jugadora':jugadora}
	return render_to_response('jugadora.html',ctx,context_instance=RequestContext(request))
