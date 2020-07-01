from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from backend.habits import views


ROUTER = routers.DefaultRouter(trailing_slash=False)
ROUTER.register('tags', views.TagViewSet)
ROUTER.register('habits', views.HabitViewSet)
ROUTER.register('entries', views.EntryViewSet)

urlpatterns = path('', include(ROUTER.urls))
