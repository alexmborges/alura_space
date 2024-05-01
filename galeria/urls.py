from django.urls import path
from galeria.views import index, imagem

# criando lista para manter todos os endereços relacioados a galera
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]