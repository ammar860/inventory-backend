from rest_framework import serializers
from api.models import Role, Permission
from .permission_serializer import PermissionSerializer
from .util import get_user_data


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)
    permissions_id = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), write_only=True, many=True)

    class Meta:
        model = Role
        fields = (
            'id', 'name', 'code_name', 'permissions', 'permissions_id', 'created_at', 'updated_at', 'created_by',
            'updated_by'
        )
        read_only_fields = (
            'created_at', 'updated_at'
        )

    def to_representation(self, instance):
        obj = instance
        instance = super().to_representation(instance)
        instance['created_by_data'] = get_user_data(obj.created_by)
        instance['updated_by_data'] = get_user_data(obj.updated_by)
        return instance

    def create(self, validated_data):
        permissions_id = validated_data.pop('permissions_id')

        role = Role.objects.create(**validated_data)
        role.permissions.set(permissions_id)
        return role

    def update(self, instance,  validated_data):
        permissions_id = validated_data.pop('permissions_id')

        instance.name = validated_data.get('name', instance.name)
        instance.code_name = validated_data.get('code_name', instance.code_name)
        instance.permissions.clear()
        instance.permissions.set(permissions_id)
        instance.save()

        return instance
