from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Jogador(models.Model):
    """Essa classe se destina para o cadastro de Jogador"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Jogador', blank = True)
    xp_total = models.FloatField(default=0, blank=True)
    m_realizadas = models.IntegerField(default=0, blank=True)
    m_adquiridas = models.IntegerField(default=0, blank=True)
    mr_nadata = models.IntegerField(default=0, blank=True)
    private_token = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return 'Jogador: %s' % (self.user.get_full_name())

class Missao(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='Jogador')
    nome_missao = models.CharField(blank=False, max_length=200)
    xp_missao = models.FloatField(blank=False)
    data = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return 'Jogador: ' + self.jogador.user.get_full_name() + ' - Missão: ' + self.nome_missao