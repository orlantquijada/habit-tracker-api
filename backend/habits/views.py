from rest_framework import mixins, viewsets

from backend.habits import serializers, models


class TagViewSet(mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):

    #pylint: disable=no-member
    queryset = models.Tag.objects
    serializer_class = serializers.base.TagSerializer

    def get_queryset(self):

        queryset = self.queryset

        serializer = serializers.query.TagQuerySerializer(
            data=self.request.query_params)

        if not serializer.is_valid():
            return queryset.all()

        user_id = serializer.validated_data.get('user_id')
        if user_id:
            queryset.filter(user_id=user_id)

        return queryset.all()
