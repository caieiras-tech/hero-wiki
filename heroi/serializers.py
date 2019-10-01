from rest_framework import serializers
from habilidade.models import Habilidade
from habilidade.serializers import HabilidadeSerializer
from hcategoria.models import Categoria
from heroi.models import Heroi
from universo.models import Universo


class UniversoData(serializers.Serializer):
    nome = serializers.CharField(read_only=True)

class CategoriaData(serializers.Serializer):
    nome = serializers.CharField(read_only=True)

class HeroiSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)
    idade = serializers.IntegerField(read_only=True)
    habilidade_heroi = HabilidadeSerializer(
        many=True,
        read_only=True,
    )
    categoria_heroi = CategoriaData()
    universo_heroi = UniversoData()

    def create(self, validated_data):
        universo_data = validated_data.pop('universo_heroi')
        universo = Universo.objects.get(id=universo_data['id'])
        categoria_data = validated_data.pop('categoria_heroi')
        categoria = Categoria.objects.get(id=categoria_data['id'])
        heroi = Heroi.objects.create(categoria_heroi=categoria, universo_heroi=universo, **validated_data)
        return heroi,

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        universo_data = validated_data.pop('universo_heroi')
        universo = Universo.objects.get(id=universo_data['id'])
        instance.universo_heroi = universo
        categoria_data = validated_data.pop('categoria_heroi')
        categoria = Categoria.objects.get(id=categoria_data['id'])
        instance.categoria_heroi = categoria
        instance.save()
        return instance