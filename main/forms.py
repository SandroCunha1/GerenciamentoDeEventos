from django import forms

from main.models import Evento

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'atracoes', 'local']
        widgets = {
            'atracoes': forms.CheckboxSelectMultiple(),
        }