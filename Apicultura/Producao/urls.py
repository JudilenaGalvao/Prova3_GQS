from django.urls import path
from Producao import views



app_name = 'Producao'

urlpatterns = [
    path('criar-criacao/', views.criar_criacao, name='criar_criacao'),
    path('listar-criacao/', views.listar_criacao, name='listar_criacao'),
    path('detalhes-criacao/<int:criacao_id>/', views.detalhes_criacao, name='detalhes_criacao'),
    path('criacao-editar/<int:criacao_id>/', views.editar_criacao, name='editar_criacao'),
    path('criar-coleta/', views.criar_coleta, name='criar_coleta'),
    path('listar-coletas/', views.listar_coletas, name='listar_coletas'),
    path('detalhes-coleta/<int:coleta_id>/', views.detalhes_coleta, name='detalhes_coleta'),
    path('coleta-editar/<int:coleta_id>/', views.editar_coleta, name='editar_coleta'),
    path('coleta-deletar/<int:coleta_id>/', views.deletar_coleta, name='deletar_coleta'),
    path('relatorio/', views.relatorio_coleta, name='relatorio_coleta'),
    path('', views.pagina_principal, name='pagina_principal'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]