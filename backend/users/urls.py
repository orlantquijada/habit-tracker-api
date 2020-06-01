from django.urls import path, include

from rest_framework import routers

from backend.users import views


ROUTER = routers.DefaultRouter()
ROUTER.register('users', views.UserViewSet)

urlpatterns = path('', include(ROUTER.urls))
