from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Evento, Local, Atracao
from .forms import AtracaoForm, CreateNewList, EventoForm, LocalForm

@login_required
def list(request, id):
    return render(request, "main/list.html", {"ls": ls})

def home(request):
    eventos = Evento.objects.all()
    return render(request, 'main/home.html', {'eventos': eventos})

@login_required
def evento_detail(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'main/evento_detail.html', {'evento': evento})

@login_required
def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    
    return render(request, "main/evento_form.html", {"form": form})

@login_required
def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'main/evento_list.html', {'eventos': eventos})

@login_required
def atracao_create(request):
    if request.method == 'POST':
        form = AtracaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atracao_list')
    else:
        form = AtracaoForm()
    
    return render(request, "main/atracao_form.html", {"form": form})

@login_required
def atracao_list(request):
    atracoes = Atracao.objects.all()
    return render(request, 'main/atracao_list.html', {'atracoes': atracoes})

def local_list(request):
    locais = Local.objects.all()
    return render(request, 'main/local_list.html', {'locais': locais})

def create_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('local-list')
    else:
        form = LocalForm()
    
    return render(request, 'main/local_form.html', {'form': form})

@login_required
def view(request):
    return render(request, "main/view.html", {})
