from django.db import models
from django.utils.translation import ugettext_lazy as _


class ThinkHazardCountry(models.Model):
    # NOTE: Naming `ThinkHazardCountry` as name originates from `ThinkHazard`
    country = models.CharField(max_length=255, verbose_name=_('country'))
    country_code = models.CharField(max_length=7, verbose_name=_('country code'))
    iso3 = models.CharField(
        max_length=3, verbose_name=_('iso3'),
        null=True, blank=True
    )  # some country have no `iso3` provided

    def __str__(self):
        return f'{self.country} - {self.iso3}'


class HazardInformation(models.Model):
    class HazardLevel(models.TextChoices):
        LOW = ' LOW', 'Low'
        VERY_LOW = 'VLO', 'Very Low'
        MEDIUM = 'MED', 'Medium'
        HIGH = 'HIG', 'High'
        NO_DATA = 'no-data', 'No Data'

    class HazardType(models.TextChoices):
        EARTHQUAKE = 'EQ', 'Earthquake'
        TSUNAMI = 'TS', 'Tsunami'
        VOLCANO = 'VO', 'Volcano'
        CYCLONES = 'CY', 'Cyclones'
        FLOODS = 'FL', 'Floods'
        URBAN_FLOODS = 'UF', 'Urban Floods'
        COASTAL_FLOODS = 'CF', 'Coastal Floods'
        LANDSLIDES = 'LS', 'Landslides'
        EXTREME_HEAT = 'EH', 'Extreme Heat'
        WILDFIRES = 'WF', 'WildFires'
        DROUGHT = 'DR', 'Drought'

    hazard_level = models.CharField(
        max_length=10, verbose_name=_('hazard level'),
        choices=HazardLevel.choices, blank=True
    )
    hazard_type = models.CharField(
        max_length=20, verbose_name=_('hazard type'),
        choices=HazardType.choices, blank=True
    )


class Hazard(models.Model):
    country = models.ForeignKey(ThinkHazardCountry, on_delete=models.CASCADE)
    hazard_informations = models.ManyToManyField(HazardInformation, blank=True)

    def __str__(self):
        return str(self.country)
