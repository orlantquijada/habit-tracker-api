from rest_framework import viewsets


class ExtendedGenericViewSet(viewsets.GenericViewSet):

    extended_serializer = None

    def get_serializer_class(self):

        extended = self.request.query_params.get('extended_data')
        extended_serializer = self.extended_serializer

        if extended and extended_serializer is not None:
            return extended_serializer

        return super().get_serializer_class()
