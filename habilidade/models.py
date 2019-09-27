from django.db import models

# Create your models here.


class Habilidade(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome habilidade'
    )

    def __str__(self):
        return self.nome

