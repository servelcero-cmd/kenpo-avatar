from django.db import models

# En este archivo se define la estructura de la base de datos.
class Technique(models.Model):
    """
    Un modelo para representar una técnica de Kenpo en la base de datos.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    source_video_url = models.URLField(max_length=500)
    generated_animation_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
