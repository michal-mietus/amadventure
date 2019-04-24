from django.urls import path
from rest_framework.authtoken import views
from . import views as auth_api_views

app_name = 'auth_api'

urlpatterns = [
    path('obtain_token/',  views.obtain_auth_token, name='obtain_token'),
    path('register/', auth_api_views.RegisterView.as_view(), name='register'),
]