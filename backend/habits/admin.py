from django.contrib import admin

from backend.habits import models


admin.site.register(models.Tag)
admin.site.register(models.Habit)
