from rest_framework import serializers
from habilidade.models import Habilidade


class HabilidadeSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)


    def create(self, validated_data):
        habilidade = Habilidade.objects.create(**validated_data)
        return habilidade

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance