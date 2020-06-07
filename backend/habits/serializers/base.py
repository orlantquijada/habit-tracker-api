from rest_framework import serializers

from backend.habits import models as habits_models
from backend.users import models as users_models


class TagSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=users_models.User.objects.all(), source='user')

    class Meta:
        model = habits_models.Tag
        fields = ('id', 'label', 'user_id')
