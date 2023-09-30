from django.shortcuts import render, redirect
from .models import Escribano, ActoJuridico
from .forms import EscribanoForm, ActoJuridicoForm
from django.contrib import messages



def index(request):
    return render(request, "index.html")


# ----- Escribanos -----

# Vista para CREAR un Escribano
def crear_escribano(request):
    if request.method == 'POST':
        form = EscribanoForm(request.POST)
        if form.is_valid():
            messages.info(request, "Escribano cargado exitosamente.")
            return redirect('crear_escribano')
    else:
        form = EscribanoForm()
    return render(request, 'crear_escribano.html', {'form': form})

# LISTAR Escribanos
# def listar_escribanos(request):
#     escribanos = Escribano.objects.all()
#     return render(request, 'listar_escribanos.html', {'escribanos': escribanos})

# ACTUALIZAR un Escribano
# def actualizar_escribano(request, pk):
#     escribano = Escribano.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EscribanoForm(request.POST, instance=escribano)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_escribanos')
#     else:
#         form = EscribanoForm(instance=escribano)
#     return render(request, 'actualizar_escribano.html', {'form': form, 'escribano': escribano})



# ----- Actos Jurídicos -----

# CREAR un ActoJuridico
def crear_acto_juridico(request):
    if request.method == 'POST':
        form = ActoJuridicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_actos_juridicos')
    else:
        form = ActoJuridicoForm()
    return render(request, 'crear_acto_juridico.html', {'form': form})

# LISTAR ActosJuridicos
def listar_actos_juridicos(request):
    actos_juridicos = ActoJuridico.objects.all()
    return render(request, 'listar_actos_juridicos.html', {'actos_juridicos': actos_juridicos})

# ACTUALIZAR un ActoJuridico
def actualizar_acto_juridico(request, pk):
    acto_juridico = ActoJuridico.objects.get(pk=pk)
    if request.method == 'POST':
        form = ActoJuridicoForm(request.POST, instance=acto_juridico)
        if form.is_valid():
            form.save()
            return redirect('listar_actos_juridicos')
    else:
        form = ActoJuridicoForm(instance=acto_juridico)
    return render(request, 'crear_acto_juridico.html', {'form': form, 'acto_juridico': acto_juridico})