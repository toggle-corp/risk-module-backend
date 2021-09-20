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
