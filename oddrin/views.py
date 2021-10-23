from rest_framework import viewsets


from oddrin.models import Oddrin
from oddrin.serializers import OddrinSerializer


class OddrinViewSet(viewsets.ModelViewSet):
    queryset = Oddrin.objects.all()
    serializer_class = OddrinSerializer
