from rest_framework import serializers
from api.models import OfficerProperty
from .util import get_user_data
from .officer_maintenance_serializer import OfficerMaintenanceSerializer


class OfficerPropertySerializer(serializers.ModelSerializer):
    maintenance = OfficerMaintenanceSerializer(many=True, read_only=True)

    class Meta:
        model = OfficerProperty
        fields = (
            'id', 'name', 'house_no', 'loc', 'unit', 'image', 'maintenance', 'created_at', 'updated_at', 'created_by',
            'type', 'updated_by'
        )
        read_only_fields = (
            'created_at', 'updated_at', 'maintenance'
        )

    def to_representation(self, instance):
        obj = instance
        instance = super().to_representation(instance)
        instance['created_by_data'] = get_user_data(obj.created_by)
        instance['updated_by_data'] = get_user_data(obj.updated_by)
        return instance

    # def create(self, validated_data):
    #     obj = OfficerProperty.objects.create(**validated_data)
    #     return obj

    # def update(self, instance,  validated_data):
    #     permissions_id = validated_data.pop('permissions_id')
    #
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.code_name = validated_data.get('code_name', instance.code_name)
    #     instance.permissions.clear()
    #     instance.permissions.set(permissions_id)
    #     instance.save()
    #
    #     return instance
