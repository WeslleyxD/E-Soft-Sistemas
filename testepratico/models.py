from django.db import models

# Create your models here.

#Model criado com ordenação crescente, primeiramente o nome e segundamente o sobrenome
class Usuarios(models.Model):
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=40)
    idade = models.CharField(max_length=2)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)
    apelido = models.CharField(max_length=50, blank=True)
    observacao = models.TextField(max_length=2000, blank=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome", 'sobrenome']
        