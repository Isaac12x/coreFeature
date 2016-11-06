from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
import views

urlpatterns = [
    # url(r'^(?P<api>[a-z | A-Z]+)', views.index, name='index'),
    url(r'^ToneAnalize/', views.ToneAnalize, name='ToneAnalize'),
    url(r'^PersonalityInsights/', views.PersonalityInsights, name='PersonalityInsights'),
	url(r'^AlchemyLanguage/', views.AlchemyLanguage, name='AlchemyLanguage'),
]


