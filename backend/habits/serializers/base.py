from rest_framework import serializers

from backend.habits import models as habits_models
from backend.users import models as users_models
from backend.utils import global_vars
from backend.utils.mixins import serializers as mixin_serializers


class TagSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=users_models.User.objects.all(), source='user')

    class Meta:
        model = habits_models.Tag
        fields = ('id', 'label', 'user_id')


class HabitSerializer(serializers.ModelSerializer, mixin_serializers.TimeStampFieldsMixinSerializer):

    allotted_time = serializers.TimeField(
        format=global_vars.TIME_FORMAT, input_formats=(global_vars.TIME_FORMAT,))

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=users_models.User.objects.all(), source='user')

    class Meta:
        inherited_fields = mixin_serializers.TimeStampFieldsMixinSerializer.Meta.fields

        model = habits_models.Habit
        fields = ('id', 'title', 'allotted_time', 'user_id') + inherited_fields
