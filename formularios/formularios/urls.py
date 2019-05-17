from django.contrib import admin
from django.conf.urls import url
from core.views import form_manual, django_form, model_form, cliente_form

urlpatterns = [
    url(r'^$', form_manual, name = 'core_form_manual'),
    url(r'^django-form/$', django_form, name = 'core_form_django'),
    url(r'^django-model-forms/$', model_form, name = 'core_django_forms'),
    url(r'^cliente/$', cliente_form, name = 'core_cliente_forms'),
    url(r'^admin/', admin.site.urls),
]
