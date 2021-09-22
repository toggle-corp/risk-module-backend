import django_filters

from think_hazard.models import Hazard


class HazardFilterSet(django_filters.FilterSet):
    country_iso3 = django_filters.CharFilter(field_name='country__iso3', lookup_expr='icontains')

    class Meta:
        model = Hazard
        fields = ('country',)
