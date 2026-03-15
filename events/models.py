from django.db import models
from people.models import Pessoa


class Encontro(models.Model):
    STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    local = models.CharField(max_length=200, blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendado')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Encontro'
        verbose_name_plural = 'Encontros'
        ordering = ['-data_inicio']

    def __str__(self):
        return self.nome


class Dia(models.Model):
    encontro = models.ForeignKey(Encontro, on_delete=models.CASCADE, related_name='dias')
    numero = models.PositiveIntegerField()
    data = models.DateField()

    class Meta:
        verbose_name = 'Dia'
        verbose_name_plural = 'Dias'
        ordering = ['numero']
        unique_together = ['encontro', 'numero']

    def __str__(self):
        return f'{self.encontro.nome} — Dia {self.numero}'


class Inscricao(models.Model):
    encontro = models.ForeignKey(Encontro, on_delete=models.CASCADE, related_name='inscricoes')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='inscricoes')
    data = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = ['encontro', 'pessoa']

    def __str__(self):
        return f'{self.pessoa.nome} — {self.encontro.nome}'


class Presenca(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='presencas')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='presencas')
    presente = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Presença'
        verbose_name_plural = 'Presenças'
        unique_together = ['dia', 'pessoa']

    def __str__(self):
        return f'{self.pessoa.nome} — {self.dia}'
