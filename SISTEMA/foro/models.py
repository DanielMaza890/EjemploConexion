from django.db import models

class Duda(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    duda = models.ForeignKey(Duda, on_delete=models.CASCADE, related_name='respuestas')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta a: {self.duda.titulo}"