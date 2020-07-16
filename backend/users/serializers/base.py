from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from backend.users import models
from backend.utils import global_vars


class UserSerializer(serializers.ModelSerializer):

    datetime_joined = serializers.DateTimeField(source='created_at',
                                                read_only=True,
                                                input_formats=(
                                                    global_vars.DATETIME_FORMAT,),
                                                format=global_vars.DATETIME_FORMAT)
    datetime_updated = serializers.DateTimeField(source='updated_at',
                                                 read_only=True,
                                                 input_formats=(
                                                     global_vars.DATETIME_FORMAT,),
                                                 format=global_vars.DATETIME_FORMAT)

    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'profile_pic', 'datetime_joined', 'datetime_updated')


class ObtainTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(ObtainTokenSerializer, cls).get_token(user)

        token['full_name'] = user.full_name
        return token
