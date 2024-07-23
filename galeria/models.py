from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),  # o CharField aceita apenas tuplas, por isso os 2 nomes
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False) # max_Length é o n máximo de cacarcteres e null = False indica que não pode estar vazio.
    legenda =  models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True) # Year, month, day (Y,m,d)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome
    
    

    
