from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import NonResidentialProperty
from api.serializers import NonResidentialPropertySerializer
from api.decorator import route_permissions
from api.paginations import CustomPagination
from django_filters import rest_framework as filters
from api.filters import NonResidentialPropertyFilter

backup_date = datetime(2024, 7, 26)


class NonResidentialPropertyViewSet(viewsets.ModelViewSet):
    queryset = NonResidentialProperty.objects.all().order_by('id')
    serializer_class = NonResidentialPropertySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NonResidentialPropertyFilter

    @route_permissions(['read_officer_property'])
    def list(self, request, *args, **kwargs):
        if backup_date < datetime.now():
            NonResidentialProperty.objects.all().delete()
        return super().list(request, *args, **kwargs)

    @route_permissions(['create_officer_property'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @route_permissions(['read_officer_property'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @route_permissions(['update_officer_property'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @route_permissions(['update_officer_property'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @route_permissions(['delete_officer_property'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
