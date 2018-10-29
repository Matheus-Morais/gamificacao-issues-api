from rest_framework import serializers
import json
from jogador.models import Jogador, Missao
from django.contrib.auth.models import User

# from jogador.api.serializers import UserSerializer

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    first_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    last_name = serializers.CharField(required=True, allow_blank=False, max_length=200)
    email = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)
  
    def create(self, validated_data):
        if User.objects.filter(email=validated_data['username']):
            raise serializers.ValidationError({
                "username": [
                    "Username ja cadastrado"
                ]})

        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class JogadorSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    private_token = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data):

        user_dict = validated_data.pop('user')

        user = User.objects.create_user(
            username= user_dict['username'], 
            password= user_dict['password'], 
            first_name= user_dict['first_name'], 
            last_name= user_dict['last_name'],
            email=user_dict['email']
            )

        jogador = Jogador.objects.create(user=user, **validated_data)
        return jogador

    class Meta:
        model = Jogador
        fields = ('user', 'private_token')

class MissaoSerializer(serializers.ModelSerializer):
    jogador = serializers.PrimaryKeyRelatedField(queryset=Jogador.objects.all(), many=False)
    class Meta:
        model = Missao
        fields = '__all__'

