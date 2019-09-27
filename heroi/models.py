from django.db import models

# Create your models here.
from habilidade.models import Habilidade
from hcategoria.models import Categoria


class Heroi(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    idade = models.IntegerField(verbose_name='Idade')
    universo = models.CharField(max_length=50, verbose_name='Universo')
    habilidade_heroi = models.ManyToManyField(
        Habilidade,
        verbose_name='habilidade',
    )
    categoria_heroi = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria',
        verbose_name='categoria',
    )

    def __str__(self):
        return self.nome