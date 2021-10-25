from django.db import models

from rest_framework import serializers

from oddrin.models import Oddrin, Idmc


class OddrinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oddrin
        fields = '__all__'


class IdmcSerializer(serializers.ModelSerializer):
    hazard_type_display = serializers.CharField(source='get_hazard_type_display')
    confidence_type_display = serializers.CharField(source='get_confidence_type_display')

    class Meta:
        model = Idmc
        fields = '__all__'
