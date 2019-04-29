from django.urls import include, path
from rest_framework import routers
from . import views


app_name = 'artifical_api'

router = routers.DefaultRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('expedition/<location_id>/', views.ExpeditionView.as_view()),
]
