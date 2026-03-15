from django.db import models
from people.models import Pessoa
# Create your models here.


class Ministerio(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Ministério'
        verbose_name_plural = 'Ministerios'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class MembroMinisterio(models.Model):
    ministerio = models.ForeignKey(
        Ministerio, on_delete=models.CASCADE, related_name='membros')
    pessoa = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, related_name='monisterio')
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Membro do Ministério'
        verbose_name_plural = 'Membros dos Ministérios'
        unique_together = ['ministério', 'pessoa']

        def __str__(self):
            return f'{self.pessoa.nome} - {self.ministerio.nome}'
