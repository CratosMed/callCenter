from django.contrib import admin
from django.urls import path, include # <--- ¡NO OLVIDES IMPORTAR INCLUDE!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ventas.urls')), # <--- Agrega esta línea
    
    # --- RUTAS DE AUTENTICACIÓN ---
    path('auth/', include('djoser.urls')),           # Para registrar usuarios, cambiar pass
    path('auth/', include('djoser.urls.authtoken')), # Para hacer Login/Logout
]