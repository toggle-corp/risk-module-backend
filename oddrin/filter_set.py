import django_filters

from oddrin.models import Idmc


class IdmcFilterSet(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')
    iso3 = django_filters.CharFilter(field_name='iso3', lookup_expr='icontains')

    class Meta:
        model = Idmc
        fields = ()
