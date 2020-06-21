from datetime import date

from django.db import models
from django.utils import timezone


class TagManager(models.Manager):

    def user(self, user_id: int):
        """ 
        Filters tags by user.

        Expects a user_id for better performance.
        """
        return self.filter(user_id=user_id)


class HabitManager(models.Manager):

    def user(self, user_id: int):
        """
        Filters habits by user.

        Expects a user_id for better performance.
        """
        return self.filter(user_id=user_id)


class EntryManager(models.Manager):

    def habit(self, habit_id: int):
        """
        Filters entries by habit.

        Expects a habit_id for better performance.
        """
        return self.filter(habit_id=habit_id)

    def entries_today(self):
        """
        Filters entries that started today.
        """
        return self.filter(datetime_started__date=timezone.now().date())

    def date_started(self, date: date):
        """
        Filters entries that started at `date`.
        """
        return self.filter(datetime_started__date=date)

    def date_ended(self, date: date):
        """
        Filters entries that ended at `date`.
        """
        return self.filter(datetime_ended__date=date)
