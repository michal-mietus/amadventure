from django.urls import include, path
from rest_framework import routers
from . import views


app_name = 'item_api'

urlpatterns = [
    path('draw/', views.ItemGetAPIView.as_view(), name='item_get'),
]
