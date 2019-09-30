from django.db import models

# Create your models here.
from habilidade.models import Habilidade
from hcategoria.models import Categoria
from universo.models import Universo


class Heroi(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    idade = models.IntegerField(verbose_name='Idade')
    habilidade_heroi = models.ManyToManyField(
        Habilidade,
        verbose_name='habilidades',
    )
    categoria_heroi = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria',
        verbose_name='categoria',
    )
    universo_heroi = models.ForeignKey(
        Universo, on_delete=models.CASCADE,
        related_name='universo',
        verbose_name='universo',
    )

    def __str__(self):
        return self.nome