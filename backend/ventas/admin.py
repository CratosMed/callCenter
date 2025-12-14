from django.contrib import admin
from .models import Venta, Telefono

# Esto permite editar los teléfonos DENTRO de la pantalla de la Venta
class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 1  # Muestra 1 espacio vacío por defecto para agregar

class VentaAdmin(admin.ModelAdmin):
    list_display = ('titular', 'documento_identidad', 'estado', 'asesor', 'fecha_creacion')
    list_filter = ('estado', 'asesor', 'es_empresa')
    search_fields = ('titular', 'documento_identidad', 'razon_social')
    inlines = [TelefonoInline] # Aquí conectamos los teléfonos

admin.site.register(Venta, VentaAdmin)