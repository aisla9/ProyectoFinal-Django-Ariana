from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Post(models.Model):
    # 1er CharField: El título del post 
    titulo = models.CharField(max_length=200)
    
    # 2do CharField: Un subtítulo 
    subtitulo = models.CharField(max_length=200)
    
    # Campo de texto enriquecido usando CKEditor
    cuerpo = RichTextField()
    
    imagen = models.ImageField(upload_to='posts_imagenes/', null=True, blank=True)
    
    # Campo de fecha que se autocompleta cuando se crea el post
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.fecha_creacion.strftime('%d/%m/%Y')}"
