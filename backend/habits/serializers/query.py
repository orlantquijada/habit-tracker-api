from rest_framework import serializers


class TagQuerySerializer(serializers.Serializer):

    user_id = serializers.IntegerField(required=False)


class HabitQuerySerializer(serializers.Serializer):

    user_id = serializers.IntegerField(required=False)


class EntryQuerySerializer(serializers.Serializer):
    pass
