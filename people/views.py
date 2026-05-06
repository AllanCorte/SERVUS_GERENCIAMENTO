from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pessoa
# Create your views here.


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()

    contexto = {
        'pessoas': pessoas,
    }
    return render(request, "pessoas/lista.html", contexto)


@login_required
def perfil_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)

    contexto = {
        'pessoa': pessoa
    }
    return render(request, 'pessoas/perfil.html', contexto)


@login_required
def nova_pessoa(request):
    if request.method == 'POST':
        Pessoa.objects.create(
            nome=request.POST.get('nome'),
            telefone=request.POST.get('telefone'),
            email=request.POST.get('email'),
            status=request.POST.get('status'),
            endereco=request.POST.get('endereco'),
            observacoes=request.POST.get('observacoes'),
        )
        return redirect('lista_pessoas')
    return render(request, 'pessoas/nova.html')


@login_required
def editar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.nome = request.POST.get('nome')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.email = request.POST.get('email')
        pessoa.status = request.POST.get('status')
        pessoa.endereco = request.POST.get('endereco')
        pessoa.observacoes = request.POST.get('observacoes')
        pessoa.save()
        return redirect('perfil_pessoa', pk=pessoa.pk)
    return render(request, 'pessoas/editar.html',
                  {'pessoa': pessoa})


@login_required
def deletar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoas')
    return render(request, 'pessoas/deletar.html',
                  {'pessoa': pessoa})
