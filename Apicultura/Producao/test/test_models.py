from django.test import TestCase
from Producao.models import Criacao, Coleta


class CriacaoModelTest(TestCase):

#Tamanho maximo caracteres
    def test_max_tamanho_raca(self):
        criacao = Criacao.objects.create(raca="a" * 51, data_entrada="2022-01-01")
        raca = criacao._meta.get_field("raca")
        max_length = raca.max_length
        self.assertEqual(max_length, 50)

#Verbose name
    def test_verbose_name_raca(self):
        raca_field = Criacao._meta.get_field("raca")
        verbose_name = raca_field.verbose_name
        self.assertEqual(verbose_name, "Raça")
#Verbose name
    def test_verbose_name_data_entrada(self):
        data_entrada_field = Criacao._meta.get_field("data_entrada")
        verbose_name = data_entrada_field.verbose_name
        self.assertEqual(verbose_name, "Data de Entrada")

#Ordenação Criação
    def test_criacao_ordem(self):
        criacao1 = Criacao.objects.create(raca="Raça 1", data_entrada="2023-01-01")
        criacao2 = Criacao.objects.create(raca="Raça 2", data_entrada="2023-02-01")
        criacao3 = Criacao.objects.create(raca="Raça 3", data_entrada="2023-03-01")

        criacoes_ordenadas = Criacao.objects.all()
        retorno_esperado = [criacao3, criacao2, criacao1]
        self.assertQuerysetEqual(criacoes_ordenadas, retorno_esperado, transform=lambda x: x)


class ColetaModelTest(TestCase):
# Verbose name
    def test_verbose_name_criacao(self):
        criacao_field = Coleta._meta.get_field("criacao")
        verbose_name = criacao_field.verbose_name
        self.assertEqual(verbose_name, "Criação")
# Verbose name
    def test_verbose_name_data(self):
        data_field = Coleta._meta.get_field("data")
        verbose_name = data_field.verbose_name
        self.assertEqual(verbose_name, "Data")
# Verbose name
    def test_verbose_name_quantidade(self):
        quantidade_field = Coleta._meta.get_field("quantidade")
        verbose_name = quantidade_field.verbose_name
        self.assertEqual(verbose_name, "Quantidade")

# Ordenação coleta
    def test_coleta_ordem(self):
        criacao = Criacao.objects.create(raca="Raça", data_entrada="2023-01-01")
        coleta1 = Coleta.objects.create(criacao=criacao, data="2023-01-01", quantidade=10)
        coleta2 = Coleta.objects.create(criacao=criacao, data="2023-02-01", quantidade=20)
        coleta3 = Coleta.objects.create(criacao=criacao, data="2023-03-01", quantidade=30)

        coletas_ordenadas = list(Coleta.objects.all())
        retorno_esperado = [coleta3, coleta2, coleta1]
        self.assertEqual(coletas_ordenadas, retorno_esperado)