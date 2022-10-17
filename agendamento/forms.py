from django import forms
from agendamento.models import Agendamento


class AgendarForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['periodo', 'equipamento', 'motivo', 'sala']
        widgets = {
            'periodo': forms.Select(
                attrs={'class': 'form-select',
                       'onchange': 'form.submit()'}
            ),
            'equipamento': forms.Select(
                attrs={'class': 'form-select',
                       'onchange': 'form.submit()'}
            ),
            'sala': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'motivo': forms.Textarea(
                attrs={'class': 'form-control', 'style': 'height: 200px;',
                       'maxlength': 450}
            ),
        }
