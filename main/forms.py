from django import forms

from main.models import Atracao, Evento, Local

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'atracoes', 'local']
        widgets = {
            'atracoes': forms.CheckboxSelectMultiple(),
        }

class AtracaoForm(forms.ModelForm):
    class Meta:
        model = Atracao
        fields = ['nome', 'descricao']

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'endereco']
        
        