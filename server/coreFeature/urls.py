from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^(?P<api>[a-z | A-Z]+)', views.index, name='index'),
    url('^$', views.index, name='index'),
]