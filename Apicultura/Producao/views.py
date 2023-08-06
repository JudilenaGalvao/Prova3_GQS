from django.shortcuts import render, redirect, get_object_or_404
from .models import Criacao, Coleta
from .forms import CriacaoForm, ColetaForm
from django.db.models import Sum
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Producao:pagina_principal')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'producao/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def listar_criacao(request):
    lista_criacao = Criacao.objects.all()
    return render(request, 'producao/listar_criacao.html', {'lista_criacao': lista_criacao})

@login_required
def criar_criacao(request):
    if request.method == 'POST':
        form = CriacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Producao:listar_criacao')
    else:
        form = CriacaoForm()
    return render(request, 'producao/criar_criacao.html', {'form': form})


@login_required
def detalhes_criacao(request, criacao_id):
    criacao = get_object_or_404(Criacao, pk=criacao_id)
    return render(request, 'producao/detalhes_criacao.html', {'criacao': criacao})


@login_required
def editar_criacao(request, criacao_id):
    criacao = get_object_or_404(Criacao, pk=criacao_id)
    if request.method == 'POST':
        form = CriacaoForm(request.POST, instance=criacao)
        if form.is_valid():
            form.save()
            return redirect('Producao:listar_criacao')
    else:
        form = CriacaoForm(instance=criacao)
    return render(request, 'producao/editar_criacao.html', {'form': form, 'criacao': criacao})



def criar_coleta(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Producao:listar_coletas')
    else:
        form = ColetaForm()
    return render(request, 'producao/criar_coleta.html', {'form': form})

@login_required
def listar_coletas(request):
    lista_coletas = Coleta.objects.all()
    return render(request, 'producao/listar_coleta.html', {'lista_coletas': lista_coletas})


@login_required
def detalhes_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, pk=coleta_id)
    return render(request, 'producao/detalhes_coleta.html', {'coleta': coleta})



def editar_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, pk=coleta_id)
    if request.method == 'POST':
        form = ColetaForm(request.POST, instance=coleta)
        if form.is_valid():
            form.save()
            return redirect('Producao:listar_coletas')
    else:
        form = ColetaForm(instance=coleta)
    return render(request, 'producao/editar_coleta.html', {'form': form, 'coleta': coleta})


@login_required
def deletar_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, pk=coleta_id)

    if request.method == 'POST':
        confirmacao = request.POST.get('confirmacao')

        if confirmacao == 'Excluir':
            coleta.delete()
            return redirect('Producao:listar_coletas')
        else:
            return redirect('Producao:listar_coletas')

    return render(request, 'Producao/deletar_coleta.html', {'coleta': coleta})


def relatorio_coleta(request):
    data_atual = datetime.now().date()

    data_inicio = data_atual - timedelta(days=365)

    coletas = Coleta.objects.filter(data__range=[data_inicio, data_atual])

    resultado = coletas.values('data__month').annotate(soma_quantidade=Sum('quantidade'))

    relatorio = []
    for item in resultado:
        mes = item['data__month']
        quantidade = item['soma_quantidade']
        relatorio.append({'mes': mes, 'quantidade': quantidade})

    context = {
        'relatorio': relatorio
    }

    return render(request, 'producao/relatorio_coleta.html', context)

@login_required
def pagina_principal(request):
    return render(request, 'base.html')
