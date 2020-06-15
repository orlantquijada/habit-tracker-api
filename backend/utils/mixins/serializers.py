from rest_framework import serializers

from backend.utils import global_vars


class TimeStampFieldsMixinSerializer(serializers.Serializer):
    """
    Assumes that the model inherits from `TimeStampFieldsMixin`.
    """

    datetime_joined = serializers.DateTimeField(source='created_at', read_only=True, input_formats=(
        global_vars.DATETIME_FORMAT,), format=global_vars.DATETIME_FORMAT)
    datetime_updated = serializers.DateTimeField(source='updated_at', read_only=True, input_formats=(
        global_vars.DATETIME_FORMAT,), format=global_vars.DATETIME_FORMAT)
