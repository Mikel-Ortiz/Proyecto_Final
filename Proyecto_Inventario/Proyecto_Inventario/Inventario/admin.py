from django.contrib import admin

from .models import Consumible, Proveedor, Reactivo

# Register your models here.
admin.site.register(Reactivo)
admin.site.register(Consumible)
admin.site.register(Proveedor)