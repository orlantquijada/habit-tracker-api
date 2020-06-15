from rest_framework import serializers

from backend.utils import global_vars


class TimeStampFieldsMixinSerializer(serializers.Serializer):
    """
    Assumes that the model inherits from `TimeStampFieldsMixin`.

    This is a convenience class for abstraction. Field names are predetermined.
    """

    created_at = serializers.DateTimeField(read_only=True, input_formats=(
        global_vars.DATETIME_FORMAT,), format=global_vars.DATETIME_FORMAT)
    updated_at = serializers.DateTimeField(read_only=True, input_formats=(
        global_vars.DATETIME_FORMAT,), format=global_vars.DATETIME_FORMAT)
