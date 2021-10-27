from rest_framework import serializers

from ipc.models import Country, GlobalDisplacement


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class GlobalDisplacementSerializer(serializers.ModelSerializer):
    country_details = CountrySerializer(source='country', read_only=True)
    hazard_type_display = serializers.CharField(source='get_hazard_type_display')

    class Meta:
        model = GlobalDisplacement
        fields = '__all__'
