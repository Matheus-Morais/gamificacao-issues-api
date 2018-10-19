from rest_framework import serializers

from jogador.models import Jogador
from django.contrib.auth.models import User

# from jogador.api.serializers import UserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name',)

class JogadorSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Jogador
        fields = '__all__'

