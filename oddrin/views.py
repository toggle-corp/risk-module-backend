from rest_framework import viewsets

from oddrin.models import (
    Oddrin,
    Idmc,
    InformRisk
)
from oddrin.serializers import (
    OddrinSerializer,
    IdmcSerializer,
    InformRiskSerializer
)
from oddrin.filter_set import (
    IdmcFilterSet,
    InformRiskFilterSet
)


class OddrinViewSet(viewsets.ModelViewSet):
    queryset = Oddrin.objects.all()
    serializer_class = OddrinSerializer


class IdmcViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Idmc.objects.all()
    serializer_class = IdmcSerializer
    filterset_class = IdmcFilterSet


class InformRiskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InformRisk.objects.all().select_related('country')
    serializer_class = InformRiskSerializer
    filterset_class = InformRiskFilterSet
