"""
URL configuration for kenpo_avatar project.
"""
from django.contrib import admin
# Asegúrese de que 'include' esté importado aquí
from django.urls import path, include

# Este es el mapa principal de URLs de la aplicación.
urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # ¡LÍNEA ACTUALIZADA! Conecta las URLs de nuestra API al proyecto principal.
    # Ahora, todas las URLs de la API comenzarán con 'api/v1/'
    path('api/v1/', include('api.urls')),
]
