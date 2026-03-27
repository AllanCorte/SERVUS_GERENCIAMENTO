from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from people.models import Pessoa
from events.models import Encontro
from nucleus.models import NotaReuniao


@login_required
def home(request):
    total_pessoas = Pessoa.objects.count()
    total_membros = Pessoa.objects.filter(status='membro').count()
    proximos_encontros = Encontro.objects.filter(status='agendado')[:3]

    ultimas_notas = NotaReuniao.objects.all()[:3]

    contexto = {
        'total_pessoas': total_pessoas,
        'total_membros': total_membros,
        'proximos_encontros': proximos_encontros,
        'ultimas_notas': ultimas_notas,
    }

    return render(request, 'core/dashboard.html', contexto)
