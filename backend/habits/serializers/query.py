from rest_framework import serializers

from backend.utils import global_vars


class TagQuerySerializer(serializers.Serializer):

    user_id = serializers.IntegerField(required=False)


class HabitQuerySerializer(serializers.Serializer):

    user_id = serializers.IntegerField(required=False)


class EntryQuerySerializer(serializers.Serializer):

    habit_id = serializers.IntegerField(required=False)

    date_started = serializers.DateField(
        required=False, format=global_vars.DATE_FORMAT, input_formats=(global_vars.DATE_FORMAT, ))
    date_ended = serializers.DateField(
        required=False, format=global_vars.DATE_FORMAT, input_formats=(global_vars.DATE_FORMAT, ))

    # convenience query param
    # should not be used with `date_started` and `date_ended`
    today = serializers.BooleanField(default=False)

