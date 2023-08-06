from django.test import TestCase
from datetime import date
from Producao.forms import ColetaForm
from Producao.models import Coleta, Criacao

class ColetaFormTest(TestCase):
    def setUp(self):
        criacao = Criacao.objects.create(raca='Criacao 1', data_entrada=date(2022, 1, 1))
        Coleta.objects.create(criacao=criacao, data=date(2022, 7, 1), quantidade=5)
#Criar coleta

    def test_criacao_coleta(self):
        form = ColetaForm(data={'criacao': Criacao.objects.first().id, 'data': '2022-01-02', 'quantidade': 10})
        self.assertTrue(form.is_valid(), form.errors)
#Criar coleta mesmo dia
    def test_criacao_coleta_mesmo_dia(self):
        form = ColetaForm(data={'criacao': 1, 'data': '2022-07-01', 'quantidade': 10})
        self.assertFalse(form.is_valid())
#Criar coleta dia futuro
    def test_criacao_coleta_dia_futuro(self):
        form = ColetaForm(data={'criacao': 1, 'data': '2024-01-01', 'quantidade': 10})
        self.assertFalse(form.is_valid())
#Editar coleta
    def test_edicao_coleta(self):
        coleta = Coleta.objects.first()
        form = ColetaForm(data={'criacao': coleta.criacao_id, 'data': '2022-07-02', 'quantidade': 10}, instance=coleta)
        self.assertTrue(form.is_valid(), form.errors)
#Edição data futura
    def test_edicao_coleta_dia_futuro(self):
        coleta = Coleta.objects.first()
        form = ColetaForm(data={'criacao': coleta.criacao_id, 'data': '2024-01-01', 'quantidade': 10}, instance=coleta)
        self.assertFalse(form.is_valid(), form.errors)
