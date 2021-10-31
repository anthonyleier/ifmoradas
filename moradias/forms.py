from django.forms import ModelForm
from moradias.models import Moradia

class MoradiaForm(ModelForm):
    class Meta:
        model = Moradia
        fields = ['nome', 'descricao', 'valor', 'imagem1', 'imagem2', 'imagem3']