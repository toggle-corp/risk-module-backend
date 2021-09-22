from rest_framework import serializers

from think_hazard.models import (
    ThinkHazardCountry,
    HazardInformation,
    Hazard
)


class ThinkHazardCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThinkHazardCountry
        exclude = ('id',)


class HazardInformationSerializer(serializers.ModelSerializer):
    hazard_level_display = serializers.CharField(source='get_hazard_level_display', read_only=True)
    hazard_type_display = serializers.CharField(source='get_hazard_type_display', read_only=True)

    class Meta:
        model = HazardInformation
        exclude = ('id',)


class HazardSerializer(serializers.ModelSerializer):
    country_details = ThinkHazardCountrySerializer(source='country')
    hazard_informations_details = HazardInformationSerializer(source='hazard_informations', many=True)

    class Meta:
        model = Hazard
        fields = '__all__'
