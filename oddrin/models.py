from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class RiskFile(models.Model):
    file = models.FileField(
        upload_to='oddrin/', max_length=255,
        null=True, blank=True, verbose_name=_('file')
    )


class Oddrin(models.Model):

    class HazardType(models.TextChoices):
        EARTHQUAKE = 'earthquake', 'Earthquake'
        FLOOD = 'flood', 'Flood'
        CYCLONE = 'cyclone', 'Cyclone'
        EPIDEMIC = 'epidemic', 'Epidemic'
        FOOD_INSECURITY = 'food_insecurity', 'Food Insecurity'
        STORM = 'storm', 'Storm'
        DROUGHT = 'drought', 'Drought'
        TSUNAMI = 'tsunami', 'Tsunami'

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        related_name='%(class)s_created',
        default=None, blank=True, null=True,
        on_delete=models.SET_NULL,
    )
    modified_by = models.ForeignKey(
        User,
        related_name='%(class)s_modified',
        default=None, blank=True, null=True,
        on_delete=models.SET_NULL,
    )
    hazard_title = models.CharField(max_length=255, verbose_name=_('hazard title'))
    hazard_type = models.CharField(max_length=100, verbose_name=_('hazard type'), choices=HazardType.choices, blank=True)
    glide_number = models.CharField(max_length=100, verbose_name=_('glide number'), null=True, blank=True)
    latitude = models.FloatField(verbose_name=_('latitude'), null=True, blank=True)
    longitude = models.FloatField(verbose_name=_('longitude'), null=True, blank=True)
    iso3 = models.CharField(max_length=3, verbose_name=_('iso3'), null=True, blank=True)
    people_exposed = models.IntegerField(verbose_name=_('people exposed'), null=True, blank=True)
    people_displaced = models.IntegerField(verbose_name=_('people displaced'), null=True, blank=True)
    buildings_exposed = models.IntegerField(verbose_name=_('buildings exposed'), null=True, blank=True)
    file = models.ForeignKey(
        RiskFile, on_delete=models.SET_NULL,
        verbose_name=_('file'),
        blank=True, null=True
    )

    def str(self):
        return f'{self.hazard_title} - {self.hazard_type}'


class Idmc(models.Model):
    class HazardType(models.TextChoices):
        FLOOD = 'flood', 'Flood'
        STORM = 'storm', 'Storm'
        FOOD_INSECURITY = 'food_insecurity', 'Food Insecurity'

    class ConfidenceType(models.TextChoices):
        HIGH = 'high', 'High'
        MEDIUM = 'medium', 'Medium'
        LOAD = 'low', 'Low'
        UNDEFINED = 'undefined', 'Undefined'

    country = models.CharField(max_length=255, verbose_name=_('country'))
    iso3 = models.CharField(max_length=3, verbose_name=_('iso3'), null=True, blank=True)
    hazard_type = models.CharField(max_length=100, verbose_name=_('hazard type'), choices=HazardType.choices, blank=True)
    confidence_type = models.CharField(
        max_length=100, verbose_name=_('confidence type'),
        choices=ConfidenceType.choices, blank=True
    )
    note = models.TextField(verbose_name=_('note'), blank=True, null=True)
    annual_average_displacement = models.FloatField(
        verbose_name=_('annual average displacement'), null=True, blank=True
    )
    january = models.FloatField(
        verbose_name=_('january'), null=True, blank=True
    )
    february = models.FloatField(
        verbose_name=_('february'), null=True, blank=True
    )
    march = models.FloatField(
        verbose_name=_('march'), null=True, blank=True
    )
    april = models.FloatField(
        verbose_name=_('april'), null=True, blank=True
    )
    may = models.FloatField(
        verbose_name=_('may'), null=True, blank=True
    )
    june = models.FloatField(
        verbose_name=_('june'), null=True, blank=True
    )
    july = models.FloatField(
        verbose_name=_('july'), null=True, blank=True
    )
    august = models.FloatField(
        verbose_name=_('august'), null=True, blank=True
    )
    september = models.FloatField(
        verbose_name=_('september'), null=True, blank=True
    )
    october = models.FloatField(
        verbose_name=_('october'), null=True, blank=True
    )
    november = models.FloatField(
        verbose_name=_('november'), null=True, blank=True
    )
    december = models.FloatField(
        verbose_name=_('december'), null=True, blank=True
    )

    def __str__(self):
        return f'{self.country} - {self.hazard_type}'


class InformRisk(models.Model):
    country = models.ForeignKey(
        'ipc.Country', on_delete=models.CASCADE,
        verbose_name=_('country'), null=True, blank=True
    )
    hazard_type = models.CharField(
        max_length=100, verbose_name=_('hazard type'),
        choices=Oddrin.HazardType.choices, blank=True
    )
    risk_score = models.FloatField(verbose_name=_('risk_score'), null=True, blank=True)

    def __str__(self):
        return f'{self.country.name} - {self.hazard_type}'


class InformRiskSeasonal(models.Model):
    country = models.ForeignKey(
        'ipc.Country', on_delete=models.CASCADE,
        verbose_name=_('country'), null=True, blank=True
    )
    hazard_type = models.CharField(
        max_length=100, verbose_name=_('hazard type'),
        choices=Oddrin.HazardType.choices, blank=True
    )
    january = models.FloatField(
        verbose_name=_('january'), null=True, blank=True
    )
    february = models.FloatField(
        verbose_name=_('february'), null=True, blank=True
    )
    march = models.FloatField(
        verbose_name=_('march'), null=True, blank=True
    )
    april = models.FloatField(
        verbose_name=_('april'), null=True, blank=True
    )
    may = models.FloatField(
        verbose_name=_('may'), null=True, blank=True
    )
    june = models.FloatField(
        verbose_name=_('june'), null=True, blank=True
    )
    july = models.FloatField(
        verbose_name=_('july'), null=True, blank=True
    )
    august = models.FloatField(
        verbose_name=_('august'), null=True, blank=True
    )
    september = models.FloatField(
        verbose_name=_('september'), null=True, blank=True
    )
    october = models.FloatField(
        verbose_name=_('october'), null=True, blank=True
    )
    november = models.FloatField(
        verbose_name=_('november'), null=True, blank=True
    )
    december = models.FloatField(
        verbose_name=_('december'), null=True, blank=True
    )

    def __str__(self):
        return f'{self.country.name} - {self.hazard_type}'


class IdmcSuddenOnset(models.Model):
    country = models.ForeignKey(
        'ipc.Country', on_delete=models.CASCADE,
        verbose_name=_('country'), null=True, blank=True
    )
    hazard_type = models.CharField(
        max_length=100, verbose_name=_('hazard type'),
        choices=Oddrin.HazardType.choices, blank=True
    )
    annual_average_displacement = models.IntegerField(
        null=True, blank=True,
        verbose_name=_('annual average displacement')
    )
    return_period_20_years = models.IntegerField(
        null=True, blank=True,
        verbose_name=_('return period 20 years')
    )
    return_period_50_years = models.IntegerField(
        null=True, blank=True,
        verbose_name=_('return period 50 years')
    )
    return_period_100_years = models.IntegerField(
        null=True, blank=True,
        verbose_name=_('return period 100 years')
    )
    return_period_250_years = models.IntegerField(
        null=True, blank=True,
        verbose_name=_('return period 250 years')
    )
    return_period_1000_years = models.IntegerField(
        null=True, blank=True,
        verbose_name=_('return period 1000 years')
    )
    return_period_1500_years = models.IntegerField(
        null=True, blank=True,
        verbose_name=_('return period 1500 years')
    )

    def __str__(self):
        return f'{self.country} - {self.hazard_type}'
