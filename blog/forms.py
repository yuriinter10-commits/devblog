from django import forms
from .models import MensagemContato

class Contatoform(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'mensagem']
        #widgets = {
            #'nome': forms.TextInput(attrs={'class': 'form-control'}),
            #'email': forms.EmailInput(attrs={'class': 'form-control'}),
            #'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
        #}