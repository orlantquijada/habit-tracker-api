from rest_framework import mixins, viewsets

from backend.users import serializers, models


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.base.UserSerializer
