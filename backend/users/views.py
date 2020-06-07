from rest_framework import mixins, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from backend.users import serializers, models


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.base.UserSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'change_password':
            return [permissions.AllowAny()]

        return super().get_permissions()

    @action(detail=False, methods=['post'], url_path='change-password')
    def change_password(self, request):
        serializer = serializers.request.ChangePasswordSerializer(
            data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_id = serializer.validated_data.get('user_id')
        try:
            user = models.User.objects.get(pk=user_id)
        # pylint: disable=no-member
        except models.User.DoesNotExist:
            return Response(data={'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        old_password = serializer.validated_data.get('old_password')
        if not user.check_password(old_password):
            return Response(data={'error': 'Old Password is incorrect.'}, status=status.HTTP_401_UNAUTHORIZED)

        new_password = serializer.validated_data.get('new_password')
        user.set_password(new_password)
        user.save()

        return Response(status=status.HTTP_200_OK)


class ObtainTokenView(TokenObtainPairView):

    serializer_class = serializers.base.ObtainTokenSerializer
    permission_classes = (permissions.AllowAny, )
