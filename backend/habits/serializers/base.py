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
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=habits_models.Tag.objects.all(),
                fields=('label', 'user_id')
            ),
        )


class HabitSerializer(serializers.ModelSerializer,
                      mixin_serializers.TimeStampFieldsMixinSerializer):

    allotted_time = serializers.TimeField(
        format=global_vars.TIME_FORMAT, input_formats=(global_vars.TIME_FORMAT,))

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=users_models.User.objects.all(), source='user')

    class Meta:
        inherited_fields = mixin_serializers.TimeStampFieldsMixinSerializer.Meta.fields

        model = habits_models.Habit
        fields = ('id', 'title', 'allotted_time', 'user_id') + inherited_fields
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=habits_models.Habit.objects.all(),
                fields=('title', 'allotted_time', 'user_id')
            ),
        )


class EntrySerializer(serializers.ModelSerializer):

    datetime_started = serializers.DateTimeField(
        format=global_vars.DATETIME_FORMAT, input_formats=(global_vars.DATETIME_FORMAT,))
    datetime_ended = serializers.DateTimeField(
        format=global_vars.DATETIME_FORMAT, input_formats=(global_vars.DATETIME_FORMAT,))

    habit_id = serializers.PrimaryKeyRelatedField(
        queryset=habits_models.Habit.objects.all(), source='habit')

    class Meta:
        model = habits_models.Entry
        fields = ('id', 'title', 'datetime_started',
                  'datetime_ended', 'habit_id')

    def validate(self, attrs):
        datetime_started = attrs.get('datetime_started')
        datetime_ended = attrs.get('datetime_ended')

        if (datetime_started and datetime_ended) and \
           (datetime_started >= datetime_ended):
            raise serializers.ValidationError(
                'Datetime Started must be before Datetime Ended!')

        return attrs
