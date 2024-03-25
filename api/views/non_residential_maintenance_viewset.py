from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import NonResidentialMaintenance
from api.serializers import NonResidentialMaintenanceSerializer
from api.decorator import route_permissions
from api.paginations import CustomPagination
from django_filters import rest_framework as filters
# from api.filters import officer_propertyFilter
backup_date = datetime(2024, 7, 26)


class NonResidentialMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = NonResidentialMaintenance.objects.all().order_by('id')
    serializer_class = NonResidentialMaintenanceSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = officer_propertyFilter

    @route_permissions(['read_officer_maintenance'])
    def list(self, request, *args, **kwargs):
        if backup_date < datetime.now():
            NonResidentialMaintenance.objects.all().delete()
        return super().list(request, *args, **kwargs)

    @route_permissions(['create_officer_maintenance'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @route_permissions(['read_officer_maintenance'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @route_permissions(['update_officer_maintenance'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @route_permissions(['update_officer_maintenance'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @route_permissions(['delete_officer_maintenance'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
