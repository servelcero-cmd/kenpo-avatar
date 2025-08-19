from django.urls import path
from .views import process_video_view

# Este es el mapa de rutas específico para nuestra API
urlpatterns = [
    # Cuando se acceda a la URL 'process-video/', se ejecutará la lógica de la vista 'process_video_view'
    path('process-video/', process_video_view, name='process-video'),
]
