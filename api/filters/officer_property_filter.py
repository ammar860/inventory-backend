import django_filters as filters
from api.models import OfficerProperty


class OfficerPropertyFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    loc = filters.CharFilter(field_name='loc')
    unit = filters.CharFilter(field_name='unit')
    type = filters.NumberFilter(field_name='type')

    class Meta:
        model = OfficerProperty
        fields = [
            'name',
            'loc',
            'unit',
            'type',
        ]
