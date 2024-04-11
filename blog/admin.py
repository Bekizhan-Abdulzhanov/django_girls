from django.contrib import admin
from apps.products.models import Post  # Импорт модели Post

admin.site.register(Post)  # Регистрация модели в админке