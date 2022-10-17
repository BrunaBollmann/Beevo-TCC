from django import forms


class Login(forms.Form):
    matricula = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'minlength': '8',
                                                                 'maxlength': '25'}))

    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                              'minlength': '8',
                                                              'maxlength': '25'}))

