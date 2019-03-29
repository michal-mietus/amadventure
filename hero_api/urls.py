from django.urls import include, path
from rest_framework import routers
from . import views


app_name = 'hero_api'

router = routers.DefaultRouter()
router.register('hero', views.HeroViewSet)
router.register('hero/(?P<hero_pk>[0-9]+)/hero_ability', views.HeroAbilityViewSet)
router.register('hero/(?P<hero_pk>[0-9]+)/statistic', views.HeroStatisticViewSet)
router.register('ability', views.AbilityViewSet)
router.register('occupation', views.OccupationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
