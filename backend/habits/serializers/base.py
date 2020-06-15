from rest_framework import serializers

from backend.habits import models as habits_models
from backend.users import models as users_models
from backend.utils import global_vars


class TagSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=users_models.User.objects.all(), source='user')

    class Meta:
        model = habits_models.Tag
        fields = ('id', 'label', 'user_id')


class HabitSerializer(serializers.ModelSerializer):

    alloted_time = serializers.TimeField(
        format=global_vars.TIME_FORMAT, input_formats=(global_vars.TIME_FORMAT,))

    datetime_joined = serializers.DateTimeField(source='created_at', read_only=True, input_formats=(
        global_vars.DATETIME_FORMAT,), format=global_vars.DATETIME_FORMAT)
    datetime_updated = serializers.DateTimeField(source='updated_at', read_only=True, input_formats=(
        global_vars.DATETIME_FORMAT,), format=global_vars.DATETIME_FORMAT)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=users_models.User.objects.all(), source='user')

    class Meta:
        model = habits_models.Habit
        fields = ('id', 'title', 'allotted_time', 'user_id',
                  'datetime_joined', 'datetime_updated')
