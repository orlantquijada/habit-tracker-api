""" Classes inside this module are assumed to be used for request bodies only. """
from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):

    user_id = serializers.IntegerField()

    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if old_password == new_password:
            raise serializers.ValidationError(
                'Your old password must not match with your new password.')

        if new_password != confirm_password:
            raise serializers.ValidationError('Passwords do not match.')

        return attrs
