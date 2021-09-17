import django_filters

from earthquake.models import Earthquake


class EarthquakeFilterSet(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')

    class Meta:
        model = Earthquake
        fields = ()
