from django.shortcuts import render, get_object_or_404, redirect
from ministries.models import Ministerio, MembroMinisterio
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def lista_ministerios(request):
    ministerios = Ministerio.objects.all()

    contexto = {
        'ministerios': ministerios,
    }
    return render(request, 'ministerios/lista.html', contexto)


@login_required
def detalhe_ministerio(request, pk):
    ministerio = get_object_or_404(Ministerio, pk=pk)
    membros = MembroMinisterio.objects.filter(ministerio=ministerio)

    contexto = {
        'ministerio': ministerio,
        'membros': membros
    }
    return render(request, 'ministerios/detalhe.html', contexto)


@login_required
def novo_ministerio(request):
    if request.method == 'POST':
        Ministerio.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
        )
        return redirect('lista_ministerios')
    return render(request, 'ministerios/novo.html')


@login_required
def editar_ministerio(request, pk):
    ministerio = get_object_or_404(Ministerio, pk=pk)
    if request.method == 'POST':
        ministerio.nome = request.POST.get('nome')
        ministerio.descricao = request.POST.get('descricao')
        ministerio.save()
        return redirect('detalhe_ministerio', pk=ministerio.pk)
    return render(request, 'ministerios/editar.html',
                  {'ministerio': ministerio})


@login_required
def deletar_ministerio(request, pk):
    ministerio = get_object_or_404(Ministerio, pk=pk)
    if request.method == 'POST':
        ministerio.delete()
        return redirect('lista_ministerios')
    return render(request, 'ministerios/deletar.html',
                  {'ministerio': ministerio})
