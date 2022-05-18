from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

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
    fields = ['nombre', 'estado_de_agregacion', 'cantidad', 'almacenamiento', 'fecha_agregado']

class ReactivoEdicion(UpdateView):
    model = Reactivo
    success_url = reverse_lazy('reactivo_listar')
    fields = ['nombre', 'estado_de_agregacion', 'cantidad', 'almacenamiento', 'fecha_agregado']

class ReactivoEliminacion(DeleteView):
    model = Reactivo
    success_url = reverse_lazy('reactivo_listar')

def busquedaReactivo(request):
    return render (request, "Inventario/busquedaReactivo.html")

def buscarReactivo(request):
    if request.GET['reactivo']:
        nombre = request.GET['reactivo']
        reactivos=Reactivo.objects.filter(nombre=nombre)
    
        return render (request, "Inventario/resultadosBusquedaReactivo.html", {"reactivos":reactivos, "nombre":nombre} )

    else:
        respuesta="No enviaste datos"

        return HttpResponse (respuesta)


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
    fields = ['nombre', 'presentacion', 'cantidad', 'area_de_trabajo', 'fecha_agregado']

class ConsumibleEdicion(UpdateView):
    model = Consumible
    success_url = reverse_lazy('consumible_listar')
    fields = ['nombre', 'presentacion', 'cantidad', 'area_de_trabajo', 'fecha_agregado']

class ConsumibleEliminacion(DeleteView):
    model = Consumible
    success_url = reverse_lazy('consumible_listar')

def busquedaConsumible(request):
    return render (request, "Inventario/busquedaConsumible.html")

def buscarConsumible(request):
    if request.GET['consumible']:
        nombre = request.GET['consumible']
        consumibles=Consumible.objects.filter(nombre=nombre)
    
        return render (request, "Inventario/resultadosBusquedaConsumible.html", {"consumibles":consumibles, "nombre":nombre} )

    else:
        respuesta="No enviaste datos"

        return HttpResponse (respuesta)

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

def busquedaProveedor(request):
    return render (request, "Inventario/busquedaProveedor.html")

def buscarProveedor(request):
    if request.GET['proveedor']:
        nombre = request.GET['proveedor']
        proveedores=Proveedor.objects.filter(nombre=nombre)
    
        return render (request, "Inventario/resultadosBusquedaProveedor.html", {"proveedores":proveedores, "nombre":nombre} )

    else:
        respuesta="No enviaste datos"

        return HttpResponse (respuesta)
