from django.db import models
from people.models import Pessoa


class NotaReuniao(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    pauta = models.TextField(blank=True)
    texto = models.TextField()
    conclusoes = models.TextField(blank=True)
    autor = models.ForeignKey(
        Pessoa, on_delete=models.SET_NULL, null=True, related_name='notas')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Nota de Reunião'
        verbose_name_plural = 'Notas de Reunião'
        ordering = ['-data']

    def __str__(self):
        return f'{self.titulo} — {self.data}'
