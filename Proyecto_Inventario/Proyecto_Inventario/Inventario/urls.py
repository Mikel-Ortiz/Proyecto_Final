from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reactivo/list', ReactivoList.as_view(), name='reactivo_listar'),
    path('reactivo/<pk>', ReactivoDetalle.as_view(), name='reactivo_detalle'),
    path('reactivo/nuevo', ReactivoCreacion.as_view(), name='reactivo_crear'),
    path('reactivo/editar/<pk>', ReactivoEdicion.as_view(), name='reactivo_editar'),
    path('reactivo/borrar/<pk>', ReactivoEliminacion.as_view(), name='reactivo_borrar'),
]