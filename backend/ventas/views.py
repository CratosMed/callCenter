from rest_framework import viewsets, permissions
from .models import Venta
from .serializers import VentaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters # Para búsqueda por texto

class VentaViewSet(viewsets.ModelViewSet):
    # Trae todas las ventas ordenadas por fecha
    queryset = Venta.objects.all().order_by('-fecha_creacion')
    serializer_class = VentaSerializer
    
    # IMPORTANTE: Solo permitir acceso si el usuario existe (está logueado)
    # Por ahora en Postman usaremos la sesión de admin, luego configuraremos Tokens.
    permission_classes = [permissions.IsAuthenticated]

    # Esta función intercepta el "Guardar"
    def perform_create(self, serializer):
        # Aquí le decimos: Guarda la venta, pero en el campo 'asesor'
        # pon al usuario que está haciendo la petición (self.request.user)
        serializer.save(asesor=self.request.user)
        
        # --- CONFIGURACIÓN DE FILTROS ---
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # 1. Filtros exactos (Ej: ?estado=PENDIENTE&asesor=2)
    filterset_fields = ['estado', 'asesor', 'es_empresa']
    
    # 2. Buscador de texto (Ej: ?search=Juan)
    # Buscará coincidencias en titular, dni o nombre de la compañía
    search_fields = ['titular', 'documento_identidad', 'nombre_compania_actual', 'razon_social']