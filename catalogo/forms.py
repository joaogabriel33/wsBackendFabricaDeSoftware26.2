from django import forms
from .models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    nota = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Avaliacao
        fields = ['jogo', 'nota', 'comentario']