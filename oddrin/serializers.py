from django.db import models

from rest_framework import serializers

from oddrin.models import (
    Oddrin,
    Idmc,
    InformRisk,
    IdmcSuddenOnset,
    InformRiskSeasonal
)
from ipc.serializers import CountrySerializer


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


class InformRiskSerializer(serializers.ModelSerializer):
    hazard_type_display = serializers.CharField(source='get_hazard_type_display')
    country_details = CountrySerializer(source='country', read_only=True)

    class Meta:
        model = InformRisk
        fields = '__all__'


class IdmcSuddenOnsetSerializer(serializers.ModelSerializer):
    hazard_type_display = serializers.CharField(source='get_hazard_type_display')
    country_details = CountrySerializer(source='country', read_only=True)

    class Meta:
        model = IdmcSuddenOnset
        fields = '__all__'


class InformRiskSeasonalSerializer(serializers.ModelSerializer):
    hazard_type_display = serializers.CharField(source='get_hazard_type_display')
    country_details = CountrySerializer(source='country', read_only=True)

    class Meta:
        model = InformRiskSeasonal
        fields = '__all__'
