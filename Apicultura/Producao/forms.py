from django import forms
from Producao.models import Criacao, Coleta
from django.utils import timezone

class ColetaForm(forms.Form):
    criacao = forms.ModelChoiceField(queryset=Criacao.objects.all())

class CriacaoForm(forms.ModelForm):
    class Meta:
        model = Criacao
        fields = ['raca', 'data_entrada']

    def clean_data_entrada(self):
        data_entrada = self.cleaned_data.get('data_entrada')
        if data_entrada and data_entrada > timezone.now().date():
            raise forms.ValidationError("Não é possivel cadastrar criações com datas futuras.")
        return data_entrada


class ColetaForm(forms.ModelForm):
    class Meta:
        model = Coleta
        fields = ['criacao', 'data', 'quantidade']

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        criacao = cleaned_data.get('criacao')
        if Coleta.objects.filter(criacao=criacao, data=data).exists():
            self.add_error('data', 'Já existe uma coleta registrada com a mesma data para essa criação.')

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data and data > timezone.now().date():
            raise forms.ValidationError("Não é possivel cadastrar coletas com datas futuras.")
        return data
