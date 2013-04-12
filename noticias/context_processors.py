from noticias.models import Noticia
from django.conf import settings


def ultimas_noticias(request):

    return dict(
        ultimas_noticias = Noticia.objects.order_by('-fecha')[:5],
    )
