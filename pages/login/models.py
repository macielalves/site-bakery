from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome_de_usuário = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.nome_de_usuário}"
