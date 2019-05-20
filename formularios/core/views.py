from django.shortcuts import render
from core.forms import NameForm, ClientForm, ClienteForm, FornecedorForm, ProdutoForm, AgendaForm

MESSAGE_REGISTRO_GRAVADO_COM_SUCESSO = 'Registro gravado com sucesso!'
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

def model_form(request):
    form = ClientForm(request.POST or None)
    message = ''
    
    if request.method == 'POST':
        form.save()
        message = 'Registro salvo com sucesso!'
        form = ClientForm()

    return render(request, 'core/django-model-forms.html', {'form':form, 'message':message})

def cliente_form(request):
    form = ClienteForm(request.POST or None)
    message = ''
    titulo = 'Cadastro de Clientes'
    if request.method == 'POST':
        form.save()
        message = MESSAGE_REGISTRO_GRAVADO_COM_SUCESSO
        form = ClienteForm()
    
    return render(request, 'core/django-model-forms.html', {'form':form, 'message':message, 'titulo':titulo})

def fornecedor_form(request):
    form = FornecedorForm(request.POST or None)
    message = ''
    titulo = 'Cadastro de Fornecedor'

    if request.method == 'POST':
        form.save()
        message = MESSAGE_REGISTRO_GRAVADO_COM_SUCESSO
        form = FornecedorForm()

    return render(request, 'core/django-model-forms.html', {'form':form, 'message':message, 'titulo':titulo})

def produto_form(request):
    form = ProdutoForm(request.POST or None)
    message = ''
    titulo = 'Cadastro de Produtos'

    if request.method == 'POST':
        form.save()
        message = MESSAGE_REGISTRO_GRAVADO_COM_SUCESSO
        form = ProdutoForm()
    
    return render(request, 'core/django-model-forms.html', {'form':form, 'message':message, 'titulo':titulo})

def agenda_form(request):
    form = AgendaForm(request.POST or None)
    message = ''
    titulo = 'Agenda Profissional'

    if request.method == 'POST':
        form.save()
        message = MESSAGE_REGISTRO_GRAVADO_COM_SUCESSO
        form = AgendaForm()
    
    return render(request, 'core/django-model-forms.html', {'form':form, 'message':message, 'titulo':titulo})