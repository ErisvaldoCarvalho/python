from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Seu nome', max_length=100)