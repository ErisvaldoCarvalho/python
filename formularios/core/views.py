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
    form = NameForm()
    return render(request, 'core/django-form.html', {'form':form})