from django.urls import path
from . import views

app_name = 'hero'

urlpatterns = [
    path('main/', views.MainView.as_view(), name='main'),
    path('create/', views.HeroCreateView.as_view(), name='hero_create'),
    path('change/statistics/', views.StatisticsChangeView.as_view(), name='statistics_change'),
    path('change/abilities/', views.AbilitiesChangeView.as_view(), name='abilities_change'),
]
