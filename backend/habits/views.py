from rest_framework import mixins

from backend.habits import serializers, models
from backend.utils import viewsets


class TagViewSet(mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.ExtendedGenericViewSet):

    queryset = models.Tag.objects
    serializer_class = serializers.base.TagSerializer
    extended_serializer_class = serializers.extended.ExtendedTagSerializer

    def get_queryset(self):
        queryset = self.queryset

        serializer = serializers.query.TagQuerySerializer(
            data=self.request.query_params)

        if not serializer.is_valid():
            return queryset.all()

        user_id = serializer.validated_data.get('user_id')
        if user_id:
            queryset = queryset.user(user_id)

        return queryset.all()


class HabitViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.ExtendedGenericViewSet):

    queryset = models.Habit.objects
    serializer_class = serializers.base.HabitSerializer
    extended_serializer_class = serializers.extended.ExtendedHabitSerializer

    def get_queryset(self):
        queryset = self.queryset

        serializer = serializers.query.HabitQuerySerializer(
            data=self.request.query_params)

        if not serializer.is_valid():
            return queryset.all()

        user_id = serializer.validated_data.get('user_id')
        if user_id:
            queryset = queryset.user(user_id)

        return queryset.all()


class EntryViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.ExtendedGenericViewSet):

    queryset = models.Entry.objects
    serializer_class = serializers.base.EntrySerializer
    extended_serializer_class = serializers.extended.ExtendedEntrySerializer

    def get_queryset(self):
        queryset = self.queryset

        serializer = serializers.query(data=self.request.query_params)

        if not serializer.is_valid():
            return queryset.all()

        habit_id = serializer.validated_data.get('habit_id')
        if habit_id:
            queryset = queryset.habit(habit_id)

        date_started = serializer.validated_data.get('date_started')
        if date_started:
            queryset = queryset.date_started(date_started)

        if date_ended := serializer.validated_data.get('date_ended'):
            queryset = queryset.date_ended(date_ended)

        return queryset.all()
