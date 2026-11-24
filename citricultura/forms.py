from django import forms
from .models import Lote
from datetime import datetime, date
from django.shortcuts import get_object_or_404

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = ["variedade", "caixas", "preco_caixa", "data", "produtor"]

    def clean_caixas(self):
        v = self.cleaned_data["caixas"]
        if v < 1:
            raise forms.ValidationError("Lote com menos de 1 caixa nao e permitido.")
        return v
    
    def clean_preco_caixa(self):
        v = self.cleaned_data["preco_caixa"]
        if v < 0:
            raise forms.ValidationError("Preco da caixa nao pode ser negativo.")
        return v
    
    def clean_data(self):
        v = self.cleaned_data["data"]
        if v < datetime.now().date():
            raise forms.ValidationError("Data nao pode ser no passado.")
        return v
