from rest_framework import serializers
from api.models import SoldierMaintenance
from .util import get_user_data


class SoldierMaintenanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoldierMaintenance
        fields = (
            'id', 'description', 'cost', 'image', 'officer_property', 'created_at', 'updated_at', 'created_by',
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
