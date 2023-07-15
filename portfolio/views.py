from datetime import datetime

from django.contrib.admin import site
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import *
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout
import time, threading
from bs4 import BeautifulSoup
import requests

from .templates.forms import *


# Create your views here.
def home_page_view(request):
    return render(request, 'portfolio/home.html')


def sobreMim_page_view(request):
    return render(request, 'portfolio/sobreMim.html')


def contactos_page_view(request):
    return render(request, 'portfolio/contactos.html')


def programacaoWeb_page_view(request):
    return render(request, 'portfolio/programacaoWeb.html')


def lista_projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/lista_projetos.html', {'projetos': projetos})


def listagem_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'login/listagem.html', {'projetos': projetos})


@login_required
def criar_projeto_view(request):
    if request.method == 'POST':
        form = AdicionarProjetoForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            fotos = form.cleaned_data['fotos']

            projeto = Projeto.objects.create(titulo=titulo, descricao=descricao)
            projeto.imagens.set(fotos)

            # Redirecionar para a página de detalhes do projeto ou outra página desejada
            return redirect('portfolio:listagem')
    else:
        form = AdicionarProjetoForm()
        return render(request, 'login/adicionar.html', {'form': form})


@login_required
def editar_projeto(request, objeto_id):
    projeto = get_object_or_404(Projeto, id=objeto_id)
    model_admin = site._registry[Projeto]
    form_class = EditarProjetoForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            imagens = form.cleaned_data['imagens']

            projeto.titulo = titulo
            projeto.descricao = descricao
            projeto.save()
            projeto.imagens.set(imagens)

            # Redirecionar para a página de detalhes do projeto ou outra página desejada
            return redirect('portfolio:listagem')
    else:
        form = form_class(initial={
            'titulo': projeto.titulo,
            'descricao': projeto.descricao,
            'imagens': projeto.imagens.all()
        })

    return render(request, 'login/editar.html', {'form': form})




@login_required
def adicionar_imagem(request):
    if request.method == 'POST':
        form = AdicionarImagemForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            imagem = form.cleaned_data['imagem']

            foto = Imagem.objects.create(nome=nome, imagem=imagem)
            return redirect('portfolio:adicionarImagem')

    else:
        form = AdicionarImagemForm()

    return render(request, 'login/adicionarImagem.html', {'form': form})

@login_required
def editar_imagem(request, objeto_id):
    imagem = get_object_or_404(Imagem, id=objeto_id)

    if request.method == 'POST':
        form = EditarImagemForm(request.POST, request.FILES)
        if form.is_valid():
            imagem.nome = form.cleaned_data['nome']
            if 'imagem' in request.FILES:
                imagem.imagem = request.FILES['imagem']
            imagem.save()
            return redirect('portfolio:listagemImagens')
    else:
        form = EditarImagemForm(initial={'nome': imagem.nome})

    return render(request, 'login/editarImagem.html', {'form': form})

def listagemImagens_view(request):
    imagens = Imagem.objects.all()
    return render(request, 'login/listagemImagens.html', {'imagens': imagens})

# user = User.objects.create_user(
#	'miguel',
#	'miguelopes1995@gmail.com',
#	'password'
# )

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "login/index.html")


@login_required
def eliminar(request, objeto_id, model, end):
    objeto = get_object_or_404(model, id=objeto_id)
    objeto.delete()
    return redirect(end)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home_admin'))
        else:
            return render(request, "login/login.html", {
                'message': "Invalid credential."
            })
    return render(request, "login/login.html")


def logout_view(request):
    logout(request)
    return render(request, 'login/login.html', {
        "message": "Logged out."
    })


def webScrapingTemperatura():
    url = 'https://weather.com/pt-PT/clima/hoje/l/f0d93b551dcc5b4eeee581ecbbc1eec1306bf6c27ea78e3c64d846a3a34969a3'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    dados = []
    localidade = soup.find('div', {'data-cq-observe': True})

    nome = localidade.find('h1').text
    temperatura_element = soup.find('span', {'data-testid': 'TemperatureValue'})
    temperatura_text = temperatura_element.text if temperatura_element else ''
    temperatura_text = temperatura_text.replace('°', '')
    temperatura = float(temperatura_text) if temperatura_text.isdigit() else 0

    dataHora = datetime.now()
    dados.append({'nome': nome, 'temperatura': temperatura, 'dataHora': dataHora})

    for dado in dados:
        novo_dado = Meteorologia(nome=dado['nome'], temperatura=dado['temperatura'], dataHora=dado['dataHora'])
        novo_dado.save()


def webScraping_page_view(request):
    #webScrapingTemperatura()
    dados = Meteorologia.objects.all()[:50]

    return render(request, 'portfolio/webscraping.html', {"dados": dados})


def agendar_metreologia_web_scraping():
    intervalo_segundos = 5 * 60 * 60
    while True:
        time.sleep(intervalo_segundos)
        webScrapingTemperatura()


t = threading.Thread(target=agendar_metreologia_web_scraping)
t.start()


def banda_page_view(request):
    bandas = Banda.objects.all()

    return render(request, 'portfolio/banda.html', {'bandas': bandas})
