from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(request):
    return render(request, 'Inventario/inicio.html')

class ReactivoList(ListView):
    model = Reactivo
    template_name = "Inventario/reactivo_list.html"

class ReactivoDetalle(DetailView):
    model = Reactivo
    template_name = "Inventario/reactivo_detalle.html"

class ReactivoCreacion(CreateView):
    model = Reactivo
    succes_url = reverse_lazy('reactivo_listar')
    fields = ['nombre', 'estado_de_agregación', 'cantidad', 'fecha_agregado']

class ReactivoEdicion(UpdateView):
    model = Reactivo
    succes_url = reverse_lazy('reactivo_listar')
    fields = ['nombre', 'estado_de_agregación', 'cantidad', 'fecha_agregado']

class ReactivoEliminacion(DeleteView):
    model = Reactivo
    succes_url = reverse_lazy('reactivo_listar')