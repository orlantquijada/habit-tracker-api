from backend.habits.serializers import base as base_habit_serializers
from backend.users.serializers import base as base_user_serializers


class ExtendedTagSerializer(base_habit_serializers.TagSerializer):

    user = base_user_serializers.UserSerializer(read_only=True)

    class Meta:
        model = base_habit_serializers.TagSerializer.Meta.model
        fields = base_habit_serializers.TagSerializer.Meta.fields + ('user',)
