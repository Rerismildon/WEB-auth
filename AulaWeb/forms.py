from django import forms
from django.core.exceptions import ValidationError
    
class TrocarSenhaForm(forms.Form):
    senha = forms.CharField(widget=forms.PasswordInput)
    conf_senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data = super().clean()
        
        if data.get('senha') != data.get('conf_senha'):
            raise ValidationError('Senhas diferentes')

        return data
    