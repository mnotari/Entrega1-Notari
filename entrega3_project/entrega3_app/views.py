from django.shortcuts import render, redirect, get_object_or_404
from .models import Objeto
from .forms import ObjetoForm
from django.db.models import Q


def index(request):
    return render(request, 'index.html')

def lista_objetos(request):
    objetos = Objeto.objects.all()
    return render(request, 'lista_objetos.html', {'objetos': objetos})

def buscar_objetos(request):
    query = request.GET.get('q')
    objetos = Objeto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query)) if query else []
    return render(request, 'buscar_objetos.html', {'objetos': objetos, 'query': query})

def agregar_objeto(request):
    if request.method == "POST":
        form = ObjetoForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            return redirect('lista_objetos')
    else:
        form = ObjetoForm()
    return render(request, 'agregar_objeto.html', {'form': form})

def editar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    if request.method == "POST":
        form = ObjetoForm(request.POST, instance=objeto)
        if form.is_valid():
            objeto = form.save()
            return redirect('lista_objetos')
    else:
        form = ObjetoForm(instance=objeto)
    return render(request, 'editar_objeto.html', {'form': form, 'objeto': objeto})

def eliminar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    objeto.delete()
    return redirect('lista_objetos')
