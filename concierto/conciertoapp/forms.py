from django import forms
from conciertoapp.models import Persona, Entrada, Concierto

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class ConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = '__all__'

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'
        widgets = {
            'concierto': forms.Select(),
            'persona': forms.Select(),
        }
