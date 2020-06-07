from django.db import models


class TagManager(models.Manager):

    def user(self, user_id: int):
        """ 
        Filters tags by user.

        Expects a user_id for better performance.
        """

        return self.filter(user_id=user_id)
