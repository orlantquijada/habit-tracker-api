from rest_framework import viewsets, serializers


class ExtendedQuerySerializer(serializers.Serializer):

    extended_data = serializers.BooleanField(required=False)


class ExtendedGenericViewSet(viewsets.GenericViewSet):

    extended_serializer_class = None

    def get_serializer_class(self):
        assert self.extended_serializer_class is not None, (
            f'{self.__class__.__name__} should include a `extended_serializer_class` attribute.')

        query_serializer = ExtendedQuerySerializer(
            data=self.request.query_params)

        if not query_serializer.is_valid():
            return super().get_serializer_class()

        if query_serializer.validated_data.get('extended_data'):
            return self.extended_serializer_class

        return super().get_serializer_class()
