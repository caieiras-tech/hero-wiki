from rest_framework import serializers

from habilidade.serializers import HabilidadeSerializer
from hcategoria.models import Categoria
from heroi.models import Heroi


class CategoriaData(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)

class HeroiSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)
    idade = serializers.IntegerField(read_only=True)
    universo = serializers.CharField(read_only=True)
    habilidade_heroi = HabilidadeSerializer(
        many=True,
        read_only=True,
    )
    categoria_heroi = CategoriaData()

    def create(self, validated_data):
        categoria_data = validated_data.pop('categoria_heroi')
        categoria = Categoria.objects.get(id=categoria_data['id'])
        heroi = Heroi.objects.create(categoria_heroi=categoria, **validated_data)
        return heroi

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance