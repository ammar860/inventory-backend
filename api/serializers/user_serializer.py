from rest_framework import serializers
from api.models import User
from .util import get_role_data, get_organization_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'name', 'role'
        )

        read_only_fields = (
            'id', 'username', 'name'
        )

    def to_representation(self, instance):
        obj = instance
        instance = super().to_representation(instance)
        instance['role_data'] = get_role_data(obj.role)
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)
        instance.role = validated_data.get('role', instance.role)
        instance.save()

        return instance
