from django.shortcuts import render
from core.forms import NameForm

def form_manual(request):
    data = {}
    if request.method == 'POST':
        data['name'] = request.POST.get('name', 'nome não encontrado')
        data['active'] = request.POST.get('active', 'off')
        data['month'] = request.POST.get('month', 'mês não encontrado')
        data['week'] = request.POST.get('week', 'semana não encontrada')
    return render(request, 'core/index.html', data)

def django_form(request):
    form = NameForm(request.POST or None)
    
    name = ''
    birth_year = ''
    favorite_colors = ''

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            birth_year = form.cleaned_data['birth_year']
            favorite_colors = form.cleaned_data['favorite_colors']

    return render(request, 'core/django-form.html', {'form':form, 'name':name, 'birth_year':birth_year,'favorite_colors':favorite_colors})