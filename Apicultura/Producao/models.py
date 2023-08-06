from django.db import models

class Criacao(models.Model):
    raca = models.CharField(max_length=50, verbose_name='Raça')
    data_entrada = models.DateField(verbose_name='Data de Entrada')

    def __str__(self):
        return str(self.data_entrada) + ", " + str(self.raca)

    class Meta:
        ordering = ['-data_entrada']


class Coleta(models.Model):
    criacao = models.ForeignKey(Criacao, on_delete=models.CASCADE, verbose_name='Criação')
    data = models.DateField(verbose_name='Data')
    quantidade = models.IntegerField(verbose_name='Quantidade')

    def _str_(self):
        return self.data

    class Meta:
        ordering = ['-data']