from rest_framework import mixins, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from backend.users import serializers, models


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.base.UserSerializer


class ObtainTokenView(TokenObtainPairView):
    serializer_class = serializers.base.ObtainTokenSerializer
    permission_classes = (permissions.AllowAny, )
