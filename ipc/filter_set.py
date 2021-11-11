import django_filters

from ipc.models import GlobalDisplacement
from oddrin.models import HazardType


class GlobalDisplacementFilterSet(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')
    iso3 = django_filters.CharFilter(field_name='country__iso3', lookup_expr='icontains')
    hazard_type = django_filters.MultipleChoiceFilter(
        choices=HazardType.choices,
        widget=django_filters.widgets.CSVWidget,
    )

    class Meta:
        model = GlobalDisplacement
        fields = ()
