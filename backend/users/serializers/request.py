from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):

    user_id = serializers.IntegerField()

    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

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
