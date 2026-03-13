from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pessoa(models.Model):
    STATUS_CHOICES = [
        ('membro', 'Membro'),
        ('visitante', 'Visitante'),
        ('inativo', 'Inativo'),
    ]

    CARGO_NUCLEO = [
        ('coordenador', 'Coordenador(a)'),
        ('secretario', 'Secretário(a)'),
        ('tesoureiro', 'Tesoureiro(a)'),
        ('lider', 'Líder'),
        ('outro', 'Outro'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='pessoa')
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='visitante')
    e_servo = models.BooleanField(default=False)
    cargo_nucleo = models.CharField(max_length=20, choices=CARGO_NUCLEO,
                                    blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_prural = 'Pessoas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    @property
    def e_nucleo(self):
        return bool(self.cargo_nucleo)
