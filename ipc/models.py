from django.db import models
from django.utils.translation import ugettext_lazy as _

from oddrin.models import Oddrin


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'), null=True, blank=True)
    iso3 = models.CharField(
        max_length=3, verbose_name=_('iso3'),
        null=True, blank=True
    )
    iso = models.CharField(
        max_length=2, verbose_name=_('iso3'),
        null=True, blank=True
    )

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.iso3:
            self.iso3 = self.iso3.lower()
        if self.iso:
            self.iso = self.iso.lower()
        return super().save(*args, **kwargs)


class Ipc(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'), null=True, blank=True)
    analysis_date = models.DateField(verbose_name=_('analysis date'), blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=_('country'),
        null=True, blank=True
    )
    phase_population = models.IntegerField(verbose_name=_('phase population'))
    census_population = models.IntegerField(verbose_name=_('census population'))
    analysis_period_start_date = models.DateField(verbose_name=_('analysis period start date'), blank=True, null=True)
    analysis_period_end_date = models.DateField(verbose_name=_('analysis period end date'), blank=True, null=True)
    hazard_type = models.CharField(max_length=100, verbose_name=_('hazard type'), choices=Oddrin.HazardType.choices, blank=True)
    is_projected = models.BooleanField(verbose_name=_('is projected'), default=False)

    def __str__(self):
        return f'{self.title} - {self.country}'


class GlobalDisplacement(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('country'))
    hazard_type = models.CharField(max_length=100, verbose_name=_('hazard type'), choices=Oddrin.HazardType.choices, blank=True)
    total_displacement = models.IntegerField(verbose_name=_('total displacement'), null=True, blank=True)
    year = models.IntegerField(verbose_name=_('year'))
    month = models.IntegerField(verbose_name=_('month'))

    def __str__(self):
        return f'{self.country} - {self.hazard_type} - {self.total_displacement}'
