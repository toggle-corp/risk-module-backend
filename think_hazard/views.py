from rest_framework import viewsets

from think_hazard.models import Hazard
from think_hazard.serializers import HazardSerializer
from think_hazard.filter_set import HazardFilterSet


class HazardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HazardSerializer
    filterset_class = HazardFilterSet

    def get_queryset(self):
        return Hazard.objects.prefetch_related(
            'hazard_informations',
            'country'
        )
