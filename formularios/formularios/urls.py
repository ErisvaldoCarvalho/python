from django.contrib import admin
from django.conf.urls import url
from core.views import form_manual

urlpatterns = [
    url(r'^$', form_manual, name = 'core_form_manual'),
    url(r'^admin/', admin.site.urls),
]
