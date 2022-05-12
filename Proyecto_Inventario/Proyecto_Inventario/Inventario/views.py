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
    success_url = reverse_lazy('reactivo_listar')
    fields = ['nombre', 'estado_de_agregacion', 'cantidad', 'almacenamiento']

class ReactivoEdicion(UpdateView):
    model = Reactivo
    success_url = reverse_lazy('reactivo_listar')
    fields = ['nombre', 'estado_de_agregacion', 'cantidad', 'almacenamiento']

class ReactivoEliminacion(DeleteView):
    model = Reactivo
    success_url = reverse_lazy('reactivo_listar')

#-----------------------------------------------------------#

class ConsumibleList(ListView):
    model = Consumible
    template_name = "Inventario/consumible_list.html"

class ConsumibleDetalle(DetailView):
    model = Consumible
    template_name = "Inventario/consumible_detalle.html"

class ConsumibleCreacion(CreateView):
    model = Consumible
    success_url = reverse_lazy('consumible_listar')
    fields = ['nombre', 'presentacion', 'cantidad', 'area_de_trabajo']

class ConsumibleEdicion(UpdateView):
    model = Consumible
    success_url = reverse_lazy('consumible_listar')
    fields = ['nombre', 'presentacion', 'cantidad', 'area_de_trabajo']

class ConsumibleEliminacion(DeleteView):
    model = Consumible
    success_url = reverse_lazy('consumible_listar')

#-----------------------------------------------------------#

class ProveedorList(ListView):
    model = Proveedor
    template_name = "Inventario/proveedor_list.html"

class ProveedorDetalle(DetailView):
    model = Proveedor
    template_name = "Inventario/proveedor_detalle.html"

class ProveedorCreacion(CreateView):
    model = Proveedor
    success_url = reverse_lazy('proveedor_listar')
    fields = ['nombre', 'apellido', 'correo', 'telefono', 'empresa']

class ProveedorEdicion(UpdateView):
    model = Proveedor
    success_url = reverse_lazy('proveedor_listar')
    fields = ['nombre', 'apellido', 'correo', 'telefono', 'empresa']

class ProveedorEliminacion(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedor_listar')