from rest_framework import serializers

from backend.users import models
from backend.utils import global_vars


class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.DateTimeField(read_only=True, input_formats=(
        global_vars.DATETIME_FORMAT,), format=global_vars.DATETIME_FORMAT)

    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'profile_pic', 'date_joined')
