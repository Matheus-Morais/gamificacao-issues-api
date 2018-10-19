from rest_framework import viewsets
from jogador.models import Jogador
from .serializers import JogadorSerializer


class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer