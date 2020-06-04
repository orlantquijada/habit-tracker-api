from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from backend.users import views


ROUTER = routers.DefaultRouter(trailing_slash=False)
ROUTER.register('users', views.UserViewSet)

urlpatterns = path('', include(ROUTER.urls))

AUTH_URLS = path('token/', include(
    [
        path('obtain', views.ObtainTokenView.as_view()),
        path('refresh',
             jwt_views.TokenRefreshView.as_view()),
        path('verify', jwt_views.token_verify)

    ]
))
