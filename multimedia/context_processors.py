from multimedia.models import Patrocinador
from django.conf import settings


def patrocinadores(request):

    return dict(
        patrocinadores = Patrocinador.objects.filter()
    )