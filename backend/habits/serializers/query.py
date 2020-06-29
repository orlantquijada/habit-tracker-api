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

    today = serializers.BooleanField(default=False)

    def validate(self, attrs):
        today = attrs.get('today')

        date_started = attrs.get('date_started')
        date_ended = attrs.get('date_ended')

        if today and (date_started or date_ended):
            return serializers.ValidationError('Do not use today` query param with `date_started` or `date_ended`.')

        return attrs
