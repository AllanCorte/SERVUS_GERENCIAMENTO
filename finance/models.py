from django.db import models
from events.models import Encontro
from people.models import Pessoa
# Create your models here.


class Entrada(models.Model):
    TIPO_CHOICES = [
        ('oferta', 'Oferta'),
        ('doacao', 'Doação'),
        ('inscricao', 'Inscrição'),
        ('outro', 'Outro'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=200, blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()
    pessoa = models.ForeignKey(
        Pessoa, on_delete=models.SET_NULL, null=True, related_name='entradas')
    encontro = models.ForeignKey(
        Encontro, onde_delet=models.SET_NULL, null=True, blank=True,
        related_name='entradas')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = [-'data']

        def __str__(self):
            return f'{self.get_tipo_display()} - R$ {self.valor}'


class Saida(models.Model):
    CATEGORIA_CHOICES = [
        ('material', 'Material'),
        ('alimentacao', 'Alimentação'),
        ('transporte', 'Transporte'),
        ('outro', 'Outro'),
    ]

    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    descricao = models.CharField(max_length=200, blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()
    encontro = models.ForeignKey(
        Encontro, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='saidas')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ' Saída'
        verbose_name_plural = 'Saídas'
        ordering = ['-data']

    def __str__(self):
        return f'{self.get_categoria_display()} - R$ {self.valor}'
