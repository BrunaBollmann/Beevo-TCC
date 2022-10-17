from django import forms
from agendamento.models import Equipamento


class CadastrarProf(forms.Form):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'minlength': '3',
                                                                        'maxlength': '30',}))

    sobrenome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'minlength': '4',
                                                                             'maxlength': '30',}))

    apelido = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'minlength': '2',
                                                                           'maxlength': '20',}))

    matricula = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'minlength': '9',
                                                                 'maxlength': '20',}))

    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                              'minlength': '8',
                                                              'maxlength': '25',}))


class CadastrarEquip(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'ativo']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control',
                       'minlength': '4',
                       'maxlength': '25'}
            ),
            'ativo': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            )
        }
