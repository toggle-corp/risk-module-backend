from django.db import models
from django.db.models.query_utils import select_related_descend
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from openpyxl.reader.excel import load_workbook


class Oddrin(models.Model):

    class HazardType(models.TextChoices):
        EARTHQUAKE = 'earthquake', 'Earthquake'
        FLOOD = 'flood', 'Flood'
        CYCLONE = 'cyclone', 'Cyclone'
        EPIDEMIC = 'epidemic', 'Epidemic'
        FOOD_INSECURITY = 'food_insecurity', 'Food Insecurity'
        STORM_SURGE = 'storm_surge', 'Storm Surge'

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

    def str(self):
        return f'{self.hazard_title} - {self.hazard_type}'


class Idmc(models.Model):
    class HazardType(models.TextChoices):
        FLOOD = 'flood', 'Flood'
        STORM = 'storm', 'Storm'

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
