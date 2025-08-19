from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def process_video_view(request):
    """
    Vista de la API para procesar un video.
    Recibe un video y un prompt, y devuelve la animación.
    """
    # Lógica futura para el procesamiento real
    video_file = request.FILES.get('video')
    prompt_text = request.data.get('prompt')

    if not video_file or not prompt_text:
        return Response(
            {"error": "Se requiere un archivo de video y un prompt."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Simulación de una respuesta exitosa para la prueba
    return JsonResponse({
        "status": "success",
        "message": "Solicitud recibida. La animación está siendo procesada.",
        "animation_url": "https://example.com/path/to/generated_video.mp4"
    })
