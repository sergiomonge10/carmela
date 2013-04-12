from uniffut.models import Equipo, Division
from django.conf import settings


def equiposprimera(request):

    return dict(
		listaequiposprimera = Equipo.objects.filter(division = "1")
    )


def equipossegunda(request):

    return dict(
        listaequipossegunda = Equipo.objects.filter(division="2")
    )