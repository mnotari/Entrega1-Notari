from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView


from .forms import AutomovilForm
from .models import Automovil


def index(request):
    return render(request, 'index.html')


def acerca_de(request):
    return render(request, 'acerca_de.html')


def lista_Automoviles(request):
    Automoviles = Automovil.objects.all()
    return render(request, 'lista_Automoviles.html', {'Automoviles': Automoviles})


def buscar_Automoviles(request):
    query = request.GET.get('q')
    Automoviles = Automovil.objects.filter(Q(marca__icontains=query)| Q(modelo__icontains=query) | Q(descripcion__icontains=query)) if query else []
    return render(request, 'buscar_automoviles.html', {'Automoviles': Automoviles, 'query': query})

@login_required
def agregar_Automovil(request):
    if request.method == "POST":
        formulario = AutomovilForm(request.POST, request.FILES)
        if formulario.is_valid():
            if formulario.cleaned_data.get('url_imagen'):
                formulario.save()
            return redirect('lista_Automoviles')
    else:
        form = AutomovilForm()
    return render(request, 'agregar_Automovil.html', {'form': form})


@login_required
def eliminar_Automovil(request, pk):
    automovil = get_object_or_404(Automovil, pk=pk)
    automovil.delete()
    return redirect('lista_Automoviles')


class editar_Automovil(LoginRequiredMixin, UpdateView):
    model = Automovil
    template_name = "editar_automovil.html"
    fields = ['marca','modelo','precio','descripcion']
    success_url = '/automoviles/'


class detalle_Automovil(DetailView):
    model = Automovil
    template_name = "detalle_automovil.html"
    
