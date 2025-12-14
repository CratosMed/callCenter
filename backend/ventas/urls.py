from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VentaViewSet

router = DefaultRouter()
router.register(r'ventas', VentaViewSet) # Esto crea la ruta /api/ventas/

urlpatterns = [
    path('', include(router.urls)),
]