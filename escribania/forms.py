from django import forms
from .models import Escribano, ActoJuridico
from django.core.exceptions import ValidationError


# class EscribanoForm(forms.ModelForm):
#     class Meta:
#         model = Escribano
#         fields = ['escribano']


class EscribanoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Escribano", required=True)
    apellido = forms.CharField(label="Apellido del Escribano", required=True)
    caracter = forms.CharField(label="Carácter", help_text="(Titular / Adscripto)", required=True)

    def clean_caracter(self):
        if self.cleaned_data["caracter"] != "Titular" and self.cleaned_data["caracter"] != "Adscripto":
            raise ValidationError("El carácter debe ser Titular o Adscripto")
        
        return self.cleaned_data["caracter"]


class ActoJuridicoForm(forms.ModelForm):
    class Meta:
        model = ActoJuridico
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Acto Jurídico'}),
        }