"""
URL configuration for kenpo_avatar project.
"""
from django.contrib import admin
from django.urls import path, include

# Este es el mapa principal de URLs de la aplicación.
# Define a qué parte del código se dirige cada solicitud.
urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # (Futuro) Aquí se conectarán las URLs de nuestra API de video.
    # Por ejemplo: path('api/v1/', include('api.urls')),
]
