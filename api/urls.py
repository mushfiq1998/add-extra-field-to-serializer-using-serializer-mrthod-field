# from django.conf.urls import url
from django.urls import path, include
from api import views
from .views import DriverViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('driver', DriverViewSet, basename='driver')

urlpatterns = [
    path('', include(router.urls)),
]
