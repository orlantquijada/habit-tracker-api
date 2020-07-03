from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from backend.utils import global_vars
from backend.utils.mixins import models as mixin_models
from backend.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin,
           mixin_models.TimeStampFieldsMixin):

    username = models.CharField(max_length=global_vars.USERNAME_MAXLENGTH,
                                unique=True)

    first_name = models.CharField('First Name',
                                  max_length=global_vars.NAME_MAXLENGTH,
                                  blank=True, null=True)
    last_name = models.CharField('Last Name',
                                 max_length=global_vars.NAME_MAXLENGTH,
                                 blank=True, null=True)

    profile_pic = models.ImageField('Profile Picture',
                                    upload_to='users/profile-pics/',
                                    blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    class Meta:
        indexes = (models.Index(fields=('username',)),)

    def __str__(self):
        return f'{self.id} / {self.username} / {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
