from rest_framework import serializers
from restaurante.models import Prato

class PratoSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Prato
        #fields = ['nome','imagem'] refere ao que vai ser serializado
        fields = '__all__'  #serializar todo o modelo