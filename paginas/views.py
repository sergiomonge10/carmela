from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from paginas.models import Tabla

def tabla_view(request):
	tabla = Tabla.objects.order_by('-puntos','-golDiferencia')
	ctx = {'tabla':tabla}
	return render_to_response('tabla.html',ctx,context_instance=RequestContext(request))