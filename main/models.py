from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Atracao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    atracoes = models.ManyToManyField(Atracao, related_name="eventos")
    local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="eventos")

    def __str__(self):
        return self.nome