from django.urls import include, path
from rest_framework import routers
from . import views


app_name = 'combat_system_api'

router = routers.DefaultRouter()
router.register('fighting_mob', views.FightingMobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
