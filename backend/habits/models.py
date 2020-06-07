from django.db import models

from backend.habits import managers
from backend.users import models as user_models
from backend.utils import global_vars


class Tag(models.Model):
    label = models.CharField(max_length=global_vars.LABEL_MAXLENGTH)

    user = models.ForeignKey(to=user_models.User, on_delete=models.CASCADE)

    objects = managers.TagManager()

    def __str__(self):
        return f'{self.user} / {self.label}'
