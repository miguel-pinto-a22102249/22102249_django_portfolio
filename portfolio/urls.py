#  hello/urls.py

from django.urls import path
from . import views
from portfolio.models import *

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('projetos', views.lista_projetos_view, name='projetos'),
    path('sobreMim', views.sobreMim_page_view, name='sobreMim'),
    path('contactos', views.contactos_page_view, name='contactos'),
    path('webScraping', views.webScraping_page_view, name='webScraping'),
    path('programacaoWeb', views.programacaoWeb_page_view, name='programacaoWeb'),
    path('home_admin', views.index, name='home_admin'),
    path('criarProjeto', views.criar_projeto_view, name='criarProjeto'),
    path('editarProjeto/<int:objeto_id>/', views.editar_projeto, name='editarProjeto'),
    path('listagem', views.listagem_view, name='listagem'),
    path('listagemImagens', views.listagemImagens_view, name='listagemImagens'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('adicionarImagem', views.adicionar_imagem, name='adicionarImagem'),
    path('editarImagem/<int:objeto_id>/', views.editar_imagem, name='editarImagem'),
    path('banda', views.banda_page_view, name='banda'),


    path('eliminarProjeto/<int:objeto_id>/', views.eliminar, {'model': Projeto, 'end': 'portfolio:listagem'}, name='eliminarProjeto'),

    path('eliminarImagem/<int:objeto_id>/', views.eliminar, {'model': Imagem, 'end': 'portfolio:listagem'}, name='eliminarImagem'),
]
