from django import forms
from django.forms import ModelForm
from moradias.models import Moradia


class MoradiaForm(ModelForm):
    class Meta:
        model = Moradia
        fields = ['nome', 'descricao', 'valor']


class ImagemForm(forms.Form):
    arquivo = forms.FileField(label='Selecione um arquivo')
