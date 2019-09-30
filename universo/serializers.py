from rest_framework import serializers

from universo.models import Universo


class UniversoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)


    def create(self, validated_data):
        universo = Universo.objects.create(**validated_data)
        return universo

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance