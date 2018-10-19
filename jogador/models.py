from django.db import models
from django.contrib.auth.models import User

class Jogador(models.Model):
    """Essa classe se destina para o cadastro de Jogador"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Jogador')
    xp = models.FloatField(default=0, blank=True)

    def __str__(self):
        return 'Jogador: %s' % (self.user.get_full_name())