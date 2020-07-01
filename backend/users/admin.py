from django.contrib import admin

from backend.users import models


admin.site.register(models.User)
