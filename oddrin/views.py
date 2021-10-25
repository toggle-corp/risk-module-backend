from rest_framework import viewsets

from oddrin.models import Oddrin, Idmc
from oddrin.serializers import OddrinSerializer, IdmcSerializer
from oddrin.filter_set import IdmcFilterSet


class OddrinViewSet(viewsets.ModelViewSet):
    queryset = Oddrin.objects.all()
    serializer_class = OddrinSerializer


class IdmcViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Idmc.objects.all()
    serializer_class = IdmcSerializer
    filterset_class = IdmcFilterSet
