from django import forms
from .models import Escribano, ActoJuridico
from django.core.exceptions import ValidationError


# class EscribanoForm(forms.ModelForm):
#     class Meta:
#         model = Escribano
#         fields = ['escribano']


from django import forms

from django import forms

class EscribanoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Escribano", required=True)
    apellido = forms.CharField(label="Apellido del Escribano", required=True)
    caracter = forms.ChoiceField(
        label="Carácter",
        choices=(("Titular", "Titular"), ("Adscripto", "Adscripto")),
        widget=forms.Select(attrs={'class': 'custom-dropdown'}),
    )


class ActoJuridicoForm(forms.ModelForm):
    class Meta:
        model = ActoJuridico
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Acto Jurídico'}),
        }