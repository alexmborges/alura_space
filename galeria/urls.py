from django.urls import path
from galeria.views import index, imagem, buscar

# criando lista para manter todos os endereços relacioados a galera
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]