from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Role
from api.serializers import RoleSerializer
from api.decorator import route_permissions
from api.paginations import CustomPagination
from django_filters import rest_framework as filters
from api.filters import RoleFilter


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.exclude(code_name='su').order_by('id')
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RoleFilter

    @route_permissions(['read_role'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @route_permissions(['create_role'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @route_permissions(['read_role'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @route_permissions(['update_role'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @route_permissions(['update_role'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @route_permissions(['delete_role'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
