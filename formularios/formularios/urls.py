from django.contrib import admin
from django.conf.urls import url
from core.views import form_manual, django_form, model_form, cliente_form, fornecedor_form, produto_form, agenda_form

urlpatterns = [
    url(r'^$', form_manual, name = 'core_form_manual'),
    url(r'^django-form/$', django_form, name = 'core_form_django'),
    url(r'^django-model-forms/$', model_form, name = 'core_django_forms'),
    url(r'^cliente/$', cliente_form, name = 'core_cliente_forms'),
    url(r'^fornecedor/$', fornecedor_form, name = 'core_fornecedor_forms'),
    url(r'^produto/$', produto_form, name = 'core_produto_forms'),
    url(r'^agenda/$', agenda_form, name = 'core_agenda_forms'),    
    url(r'^admin/', admin.site.urls),
]