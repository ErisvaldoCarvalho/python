from django.contrib import admin
from django.conf.urls import url
from core.views import form_manual, django_form

urlpatterns = [
    url(r'^$', form_manual, name = 'core_form_manual'),
    url(r'^django-form/$', django_form,'core_from_django'),
    url(r'^admin/', admin.site.urls),
]
