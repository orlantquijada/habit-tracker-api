from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from backend.habits import views


ROUTER = routers.DefaultRouter(trailing_slash=False)
ROUTER.register('tags', views.TagViewSet)

urlpatterns = path('', include(ROUTER.urls))
