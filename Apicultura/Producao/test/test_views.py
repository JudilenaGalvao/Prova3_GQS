from django.test import TestCase
from django.contrib.auth.models import User
from Producao.models import Criacao, Coleta
from Producao import views
import random
from django.urls import reverse
from datetime import date
from django.test.client import Client


class ColetaViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Criacao 1', data_entrada="2022-01-01")
        Criacao.objects.create(raca='Criacao 2', data_entrada="2022-01-02")
        Coleta.objects.create(criacao=Criacao.objects.first(), data="2022-07-01", quantidade=5)
        Coleta.objects.create(criacao=Criacao.objects.first(), data="2022-07-02", quantidade=10)
        Coleta.objects.create(criacao=Criacao.objects.last(), data="2022-07-03", quantidade=15)

#Se URL coletas está correta
    def test_listar_coletas_url(self):
        response = self.client.get(reverse('Producao:listar_coletas'))
        self.assertEqual(response.status_code, 200)
#Se template coletas está correto
    def test_listar_coleta_template(self):
        response = self.client.get(reverse('Producao:listar_coletas'))
        self.assertTemplateUsed(response, 'producao/listar_coleta.html')
#Listar todas coletas
    def test_listar_coleta_all(self):
        response = self.client.get(reverse('Producao:listar_coletas'))
        self.assertEquals(len(response.context['lista_coletas']), 3)
#Se detalhes da coleta está correta
    def test_detalhes_coletas_url(self):
        response = self.client.get(reverse('Producao:detalhes_coleta', args=[1])) #Testando com ID = 1
        self.assertEqual(response.status_code, 200)
#Se template de detalhes da coleta está correto
    def test_detalhes_coleta_template(self):
        response = self.client.get(reverse('Producao:detalhes_coleta', args=[1])) #Testando com ID = 1
        self.assertTemplateUsed(response, 'producao/detalhes_coleta.html')
#Mostra detalhes do objeto correto
    def test_detalhes_coleta(self):
        response = self.client.get(reverse('Producao:detalhes_coleta', args=[1])) #Testando com ID = 1
        objeto = response.context['coleta']
        self.assertEqual(objeto, Coleta.objects.get(id=1))
#Deletar coleta URL
    def test_deletar_coleta_url(self):
        response = self.client.get(reverse('Producao:deletar_coleta', args=[3])) #Testando com ID = 1
        self.assertEqual(response.status_code, 302) #200 #Não é 200 pois o django redireciona, por isso 302, como se pedisse página de confirmação do delete.

#Deletar coleta template
#TEM QUE CRIAR HTML PRA DELETAR COLETA?
    def test_deletar_coleta_template(self):
        response = self.client.get(reverse('Producao:deletar_coleta', args=[3])) #Testando com ID = 1
        self.assertTemplateUsed(response, 'producao/deletar_coleta.html')

#Deletar coleta indicada
    def test_deletar_coleta(self):
        response = self.client.post(reverse('Producao:deletar_coleta', args=[3]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('Producao:listar_coletas'))
        self.assertFalse(Coleta.objects.filter(id=3).exists())


class CriarColetaTest(TestCase):
    def test_criar_coleta_url(self):
        url = reverse('Producao:criar_coleta')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_criar_coleta_template(self):
        url = reverse('Producao:criar_coleta')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'producao/criar_coleta.html')

    def test_criar_coleta_criacao_objeto(self):
        criacao = Criacao.objects.create(raca="Raça", data_entrada=date.today())
        form_data = {
            'criacao': criacao.pk,
            'data': date.today(),
            'quantidade': 10
        }
        url = reverse('Producao:criar_coleta')
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Coleta.objects.count(), 1)



class ColetaViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Criacao 1', data_entrada="2022-01-01")
        Criacao.objects.create(raca='Criacao 2', data_entrada="2022-01-02")
        Coleta.objects.create(criacao=Criacao.objects.first(), data="2022-07-01", quantidade=5)
        Coleta.objects.create(criacao=Criacao.objects.first(), data="2022-07-02", quantidade=10)
        Coleta.objects.create(criacao=Criacao.objects.last(), data="2022-07-03", quantidade=15)

#    def setUp(self):
#        self.client = Client()
#        usuario = User.objects.create_user(username="testuser", password="123")
#        self.client.login(username="testuser", password="123")

    def test_criar_coleta_url(self):
        response = self.client.get(reverse('Producao:criar_coleta'))
        self.assertEqual(response.status_code, 200)

    def test_criar_coleta_template(self):
        response = self.client.get(reverse('Producao:criar_coleta'))
        self.assertTemplateUsed(response, 'producao/criar_coleta.html')

    def test_criar_coleta_cria_objeto(self):
        criacao = Criacao.objects.create(raca="Raça", data_entrada="2023-01-01")
        form_data = {
            'criacao': criacao.pk,
            'data': "2023-07-01",
            'quantidade': 10
        }
        response = self.client.post(reverse('Producao:criar_coleta'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Coleta.objects.count(), 4)  # Verifica se o objeto foi criado corretamente

    def test_editar_coleta_url(self):
        coleta = Coleta.objects.first()
        response = self.client.get(reverse('Producao:editar_coleta', args=[coleta.pk]))
        self.assertEqual(response.status_code, 200)

    def test_editar_coleta_template(self):
        coleta = Coleta.objects.first()
        response = self.client.get(reverse('Producao:editar_coleta', args=[coleta.pk]))
        self.assertTemplateUsed(response, 'producao/editar_coleta.html')

    def test_editar_coleta_edita_objeto(self):
        coleta = Coleta.objects.first()
        form_data = {
            'criacao': coleta.criacao.pk,
            'data': "2022-07-01",
            'quantidade': 15
        }
        response = self.client.post(reverse('Producao:editar_coleta', args=[coleta.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)
        coleta.refresh_from_db()
        self.assertEqual(coleta.quantidade, 15)  # Verifica se o objeto foi editado corretamente

    def test_exibir_relatorio_coleta_url(self):
        response = self.client.get(reverse('Producao:relatorio_coleta'))
        self.assertEqual(response.status_code, 200)

    def test_exibir_relatorio_coleta_template(self):
        response = self.client.get(reverse('Producao:relatorio_coleta'))
        self.assertTemplateUsed(response, 'producao/relatorio_coleta.html')


    def test_relatorio_coleta_exibe_corretamente(self):
        criacao = Criacao.objects.create(raca="Raça", data_entrada=date(2023, 7, 4))

        coleta1 = Coleta.objects.create(criacao=criacao, data=date(2023, 7, 4), quantidade=10)
        coleta2 = Coleta.objects.create(criacao=criacao, data=date(2023, 7, 4), quantidade=15)

        url = reverse('Producao:relatorio_coleta')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        relatorio = response.context['relatorio']
        self.assertEqual(len(relatorio), 1)
        self.assertEqual(relatorio[0]['mes'], 7)
        self.assertEqual(relatorio[0]['quantidade'], coleta1.quantidade + coleta2.quantidade)
