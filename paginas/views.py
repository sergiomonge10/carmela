from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from paginas.models import TablaPrimera,TablaSegunda,Partido
from paginas.forms import ContactForm
from django.core.mail import EmailMultiAlternatives

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

def contacto_view(request):
	info_send = False #define si se envia la informacion
	email = ""
	title = ""
	text = ""
	if request.method == 'POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_send = True
			email = formulario.cleaned_data['Email']
			title = formulario.cleaned_data['Title']
			text = formulario.cleaned_data['Text']

			#Configuracion enviando mensaje via GMAIL

			to_admin = 'pruebaspruebas16@gmail.com'
			html_content = "Informacion Recibida de [%s] <br><br><br>***Mensaje***<br><br>%s"%(email,text)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = ContactForm()

	ctx = {'form':formulario,'email':email,'title':title,'text':text,'info_send':info_send}
	return render_to_response('contacto.html',ctx,context_instance=RequestContext(request))

def nosotros_view(request):
	return render_to_response('nosotros.html',context_instance=RequestContext(request))