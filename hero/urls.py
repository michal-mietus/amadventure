from django.urls import path
from . import views

app_name = 'hero'

urlpatterns = [
    path('create/', views.HeroCreateView.as_view(), name='hero_create'),
]
