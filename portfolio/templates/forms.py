from django import forms
from ..models import *


class AdicionarProjetoForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    descricao = forms.CharField(widget=forms.Textarea)
    fotos = forms.ModelMultipleChoiceField(
        queryset=Imagem.objects.all(),
        widget=forms.SelectMultiple
    )


class EditarProjetoForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    descricao = forms.CharField(widget=forms.Textarea)
    imagens = forms.ModelMultipleChoiceField(
        queryset=Imagem.objects.all(),
        widget=forms.SelectMultiple
    )



class AdicionarImagemForm(forms.Form):
    nome = forms.CharField(max_length=255)
    imagem = forms.ImageField()

class EditarImagemForm(forms.Form):
    nome = forms.CharField(max_length=255)
    imagem = forms.ImageField()