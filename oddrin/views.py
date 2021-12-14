from rest_framework import viewsets

from oddrin.models import (
    Oddrin,
    Idmc,
    InformRisk,
    IdmcSuddenOnset,
    InformRiskSeasonal,
    DisplacementData,
    GarHazard,
    PdcDisplacement
)
from oddrin.serializers import (
    OddrinSerializer,
    IdmcSerializer,
    InformRiskSerializer,
    IdmcSuddenOnsetSerializer,
    InformRiskSeasonalSerializer,
    DisplacementDataSerializer,
    GarHazardSerializer,
    PdcDisplacementSerializer
)
from oddrin.filter_set import (
    IdmcFilterSet,
    InformRiskFilterSet,
    IdmcSuddenOnsetFilterSet,
    InfromRiskSeasonalFilterSet,
    OddrinFilterSet,
    DisplacementDataFilterSet,
    GarHazardFilterSet,
    PdcDisplacemenFilterSet
)


class OddrinViewSet(viewsets.ModelViewSet):
    queryset = Oddrin.objects.all()
    serializer_class = OddrinSerializer
    filterset_class = OddrinFilterSet


class IdmcViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Idmc.objects.all()
    serializer_class = IdmcSerializer
    filterset_class = IdmcFilterSet


class InformRiskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InformRisk.objects.select_related('country')
    serializer_class = InformRiskSerializer
    filterset_class = InformRiskFilterSet


class IdmcSuddenOnsetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IdmcSuddenOnset.objects.select_related('country')
    serializer_class = IdmcSuddenOnsetSerializer
    filterset_class = IdmcSuddenOnsetFilterSet


class InformRiskSeasonalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InformRiskSeasonal.objects.select_related('country')
    serializer_class = InformRiskSeasonalSerializer
    filterset_class = InfromRiskSeasonalFilterSet


class DisplacementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DisplacementData.objects.select_related('country')
    serializer_class = DisplacementDataSerializer
    filterset_class = DisplacementDataFilterSet


class GarHazardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GarHazard.objects.select_related('country')
    serializer_class = GarHazardSerializer
    filterset_class = GarHazardFilterSet


class PdcDisplacementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PdcDisplacement.objects.select_related('country')
    serializer_class = PdcDisplacementSerializer
    filterset_class = PdcDisplacemenFilterSet
