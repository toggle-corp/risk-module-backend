from rest_framework import viewsets

from ipc.models import GlobalDisplacement
from ipc.serializers import GlobalDisplacementSerializer
from ipc.filter_set import GlobalDisplacementFilterSet


class GlobalDisplacementViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GlobalDisplacementSerializer
    filterset_class = GlobalDisplacementFilterSet
    queryset = GlobalDisplacement.objects.all()
