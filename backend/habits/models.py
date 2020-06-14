from django.db import models

from backend.habits import managers
from backend.users import models as user_models
from backend.utils import global_vars
from backend.utils.mixins import models as mixin_models


class Tag(models.Model):

    label = models.CharField(max_length=global_vars.LABEL_MAXLENGTH)

    user = models.ForeignKey(to=user_models.User, on_delete=models.CASCADE)

    objects = managers.TagManager()

    class Meta:
        constraints = (models.UniqueConstraint(
            fields=('label', 'user'), name='unique_tags'),)

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.id} / {self.user.full_name} / {self.label}'


class Habit(mixin_models.TimeStampFieldsMixin):

    title = models.CharField(max_length=global_vars.HABIT_TITLE_MAXLENGTH)
    allotted_time = models.TimeField('Allotted Time')

    user = models.ForeignKey(to=user_models.User, on_delete=models.CASCADE)

    objects = managers.HabitManager()

    class Meta:
        constraints = (models.UniqueConstraint(
            fields=('title', 'allotted_time', 'user'), name='unique_habits'),)

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.id} / {self.user.full_name} / {self.title}'
