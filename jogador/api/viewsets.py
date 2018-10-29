from rest_framework import viewsets

from jogador.models import Jogador, Missao
from django.contrib.auth.models import User
from .serializers import JogadorSerializer, UserSerializer, MissaoSerializer


class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MissaoViewSet(viewsets.ModelViewSet):
    queryset = Missao.objects.all()
    serializer_class = MissaoSerializer