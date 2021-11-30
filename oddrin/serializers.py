from rest_framework import serializers

from oddrin.models import (
    Oddrin,
    Idmc,
    InformRisk,
    IdmcSuddenOnset,
    InformRiskSeasonal,
    RiskFile
)
from ipc.serializers import CountrySerializer
from oddrin.scripts.create_raster_tile import create_raster_tile


class RiskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFile
        fields = '__all__'


class OddrinSerializer(serializers.ModelSerializer):
    hazard_type_display = serializers.CharField(source='get_hazard_type_display', read_only=True)
    file_type_display = serializers.CharField(source='get_file_type_display', read_only=True)

    class Meta:
        model = Oddrin
        fields = '__all__'

    """def create(self, validate_data):
        file = validate_data.get('file')
        glide_number = validate_data.get('glide_number')
        if file:
            mapbox_layer_id = create_raster_tile(file)
        data = super().create(validate_data)
        data['mapbox_layer_id'] = mapbox_layer_id
        return data"""


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
