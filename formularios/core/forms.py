from django import forms
from django.forms import ModelForm
from core.models import Client

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984')
FAVORITE_COLORS_CHOICES = (
    ('azul', 'Azul'),
    ('verde', 'Verde'),
    ('preto', 'Preto'),
    )

class NameForm(forms.Form):
    name = forms.CharField(label='Seu nome', max_length=100)
    birth_year = forms.DateField(widget = forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'birth_year', 'birth_year1', 'favorite_colors']