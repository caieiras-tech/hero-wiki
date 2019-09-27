from rest_framework import serializers

from hcategoria.models import Categoria


class CategoriaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)


    def create(self, validated_data):
        categoria = Categoria.objects.create(**validated_data)
        return categoria

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance