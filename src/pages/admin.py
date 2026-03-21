from django.contrib import admin
from .models import Post

# Registramos el modelo para que aparezca en el panel
admin.site.register(Post)
