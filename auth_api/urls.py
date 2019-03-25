from django.urls import path
from rest_framework.authtoken import views

app_name = 'auth_api'

urlpatterns = [
    path('obtain_token/',  views.obtain_auth_token, name='obtain_token'),
]