from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ipc(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    country_code = models.CharField(max_length=3, verbose_name=_('code'))
    analysis_date = models.DateField(verbose_name=_('analysis date'), blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name=_('country'))
    phase_popultion = models.IntegerField(verbose_name=_('phase population'))
    census_population = models.IntegerField(verbose_name=_('census population'))
    current_from_date = models.DateField(verbose_name=_('current from date'), blank=True, null=True)
    current_to_date = models.DateField(verbose_name=_('current to date'), blank=True, null=True)
    projected_from_date = models.DateField(verbose_name=_('projected from date'), blank=True, null=True)
    projected_to_date = models.DateField(verbose_name=_('projected to date'), blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.country}'
