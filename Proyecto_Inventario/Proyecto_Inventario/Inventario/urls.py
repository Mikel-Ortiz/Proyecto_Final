from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),

    path('reactivo/list/', ReactivoList.as_view(), name='reactivo_listar'),
    path('reactivo/<pk>', ReactivoDetalle.as_view(), name='reactivo_detalle'),
    path('reactivo/nuevo/', ReactivoCreacion.as_view(), name='reactivo_crear'),
    path('reactivo/editar/<pk>', ReactivoEdicion.as_view(), name='reactivo_editar'),
    path('reactivo/borrar/<pk>', ReactivoEliminacion.as_view(), name='reactivo_borrar'),
    path('busquedaReactivo/', busquedaReactivo, name='BusquedaReactivo'),
    path('buscar/', buscarReactivo),

    path('consumible/list/', ConsumibleList.as_view(), name='consumible_listar'),
    path('consumible/<pk>', ConsumibleDetalle.as_view(), name='consumible_detalle'),
    path('consumible/nuevo/', ConsumibleCreacion.as_view(), name='consumible_crear'),
    path('consumible/editar/<pk>', ConsumibleEdicion.as_view(), name='consumible_editar'),
    path('consumible/borrar/<pk>', ConsumibleEliminacion.as_view(), name='consumible_borrar'),
    path('busquedaConsumible/', busquedaConsumible, name='BusquedaConsumible'),
    path('buscar2/', buscarConsumible),

    path('proveedor/list/', ProveedorList.as_view(), name='proveedor_listar'),
    path('proveedor/<pk>', ProveedorDetalle.as_view(), name='proveedor_detalle'),
    path('proveedor/nuevo/', ProveedorCreacion.as_view(), name='proveedor_crear'),
    path('proveedor/editar/<pk>', ProveedorEdicion.as_view(), name='proveedor_editar'),
    path('proveedor/borrar/<pk>', ProveedorEliminacion.as_view(), name='proveedor_borrar'),
    path('busquedaProveedor/', busquedaProveedor, name='BusquedaProveedor'),
    path('buscar3/', buscarProveedor),
]