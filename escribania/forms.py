from django import forms
from .models import Escribano, ActoJuridico


class EscribanoForm(forms.ModelForm):
    class Meta:
        model = Escribano
        fields = ['escribano']

class ActoJuridicoForm(forms.ModelForm):
    class Meta:
        model = ActoJuridico
        fields = ['nombre']