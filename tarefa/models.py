from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField()
    ativo = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=False)
    
    def __str__(self):
        return self.titulo