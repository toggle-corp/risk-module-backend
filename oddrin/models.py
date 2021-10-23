from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


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
