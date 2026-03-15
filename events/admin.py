from django.contrib import admin
from .models import Encontro, Dia, Inscricao, Presenca
# Register your models here.

admin.site.register(Encontro)
admin.site.register(Dia)
admin.site.register(Inscricao)
admin.site.register(Presenca)
