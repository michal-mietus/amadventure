from django.urls import include, path
from rest_framework import routers
from . import views


app_name = 'hero_api'

router = routers.DefaultRouter()
router.register('hero', views.HeroViewSet)
router.register('owned', views.HeroAllDataViewSet, basename="hero_all_data")
router.register('(?P<hero_pk>[0-9]+)/hero_ability', views.HeroAbilityViewSet)
router.register('(?P<hero_pk>[0-9]+)/statistic', views.HeroStatisticViewSet)
router.register('ability', views.AbilityViewSet)
router.register('occupation', views.OccupationViewSet)
router.register('occupation/(?P<occupation_pk>[0-9]+)/ability/all', views.OccupationAbilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.HeroCreateView.as_view(), name='hero_create'),
    path('statistic/all/upgrade/', views.HeroStatisticAllUpgrade.as_view(), name="statistic_all_upgrade"),
    path('ability/all/upgrade/', views.HeroAbilityAllUpgrade.as_view(), name="ability_all_upgrade"),
    path('upgrade/', views.HeroUpgradeView.as_view(), name='hero_upgrade'),
    path('item/add/', views.HeroAddItemView.as_view(), name='hero_add_item'),
]
