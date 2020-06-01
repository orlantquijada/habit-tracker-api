from django.contrib import admin
from django.urls import path, include

from backend.users.urls import urlpatterns as USERS_URLS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(
        (
            USERS_URLS,
        )
    ))
]
