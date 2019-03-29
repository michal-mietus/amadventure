from django.urls import path
from . import views

app_name = 'hero'

urlpatterns = [
    path('main/', views.MainView.as_view(), name='main'),
    path('create/', views.HeroCreateView.as_view(), name='hero_create'),
    path('change/statistics/', views.HeroStatisticsUpdateView.as_view(), name='statistics_update'),
    path('change/abilities/', views.AbilitiesUpdateView.as_view(), name='abilities_update'),
]
