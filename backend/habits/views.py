from rest_framework import mixins

from backend.habits import serializers, models
from backend.utils import viewsets


class TagViewSet(mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.ExtendedGenericViewSet):

    #pylint: disable=no-member
    queryset = models.Tag.objects
    serializer_class = serializers.base.TagSerializer
    extended_serializer = serializers.extended.ExtendedTagSerializer

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
