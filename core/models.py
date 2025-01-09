from django.db import models

class Profissional (models.Model):
    nome_completo = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True)
    profissao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=500)
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_completo
    
class Consulta(models.Model):
    data = models.DateTimeField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name="consultas" )

    def __str__(self):
        return f"Consulta de {self.profissional.nome_completo} em {self.data}"