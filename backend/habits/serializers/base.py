from rest_framework import serializers

from backend.habits import models


class TagSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(source='user')

    class Meta:
        model = models.Tag
        fields = ('id', 'label', 'user')
