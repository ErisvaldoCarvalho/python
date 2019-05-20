from django.contrib import admin
from core.models import Client, Cliente, Fornecedor, Produto, Agenda

class AgendaInline(admin.TabularInline):
    model = Agenda
    extra = 1

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome']}),
        (None, {'fields': ['cpf']}),
        (None, {'fields': ['sexo']}), 
        (None, {'fields': ['fone']}), 
        (None, {'fields': ['email']}), 
        (None, {'fields': ['endereco']}), 
    ]
    inlines = [AgendaInline]
    list_display = ['nome', 'cpf', 'sexo','fone', 'email', 'endereco']
    list_filter = ['sexo']
    search_fields = ['nome', 'cpf', 'sexo', 'fone', 'email', 'endereco']

class AgendaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['descricao']}),
        (None, {'fields': ['dataInicial']}),
        (None, {'fields': ['dataFinal']}),
        (None, {'fields': ['cliente']}), 
    ]
    
    list_display = ['cliente', 'descricao', 'dataInicial', 'dataFinal']
    list_filter = ['descricao', 'dataInicial', 'dataFinal']
    search_fields = ['descricao', 'dataInicial', 'dataFinal']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Agenda, AgendaAdmin)