from backend.habits.serializers import base as base_habit_serializers
from backend.users.serializers import base as base_user_serializers


class ExtendedTagSerializer(base_habit_serializers.TagSerializer):

    user = base_user_serializers.UserSerializer(read_only=True)

    class Meta:
        model = base_habit_serializers.TagSerializer.Meta.model
        fields = base_habit_serializers.TagSerializer.Meta.fields + ('user',)


class ExtendedHabitSerializer(base_habit_serializers.TagSerializer):

    user = base_user_serializers.UserSerializer(read_only=True)

    class Meta:
        model = base_habit_serializers.HabitSerializer.Meta.model
        fields = base_habit_serializers.HabitSerializer.Meta.fields + ('user',)


class ExtendedEntrySerializer(base_habit_serializers.EntrySerializer):

    habit = ExtendedHabitSerializer(read_only=True)

    class Meta:
        model = base_habit_serializers.EntrySerializer.Meta.model
        fields = base_habit_serializers.EntrySerializer.Meta.fields + \
            ('habit',)
