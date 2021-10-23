from rest_framework import serializers

from oddrin.models import Oddrin


class OddrinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oddrin
        fields = '__all__'
