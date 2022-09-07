from django.db import models

# Create your models here.
class Prato(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=18)
    imagem = models.ImageField(blank=True)

#mostrar os nome

    def __str__(self):
        return self.nome
