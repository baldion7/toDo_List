from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En Proceso'),
            ('completado', 'Completado'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendiente',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
