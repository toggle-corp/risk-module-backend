from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_enumfield import enum


class Earthquake(models.Model):

    class MagnitudeType(enum.Enum):
        TWO = 0
        FOUR = 1
        FA = 2
        H = 3
        LG = 4
        M = 5
        MA = 6
        mb = 7
        MBLG = 8
        MB_LG = 9
        MC = 10
        MD = 11
        MDL = 12
        ME = 13
        MFA = 14
        MH = 15
        MI = 116
        MINT = 17
        ML = 18
        MLG = 19
        MLR = 20
        MLV = 21
        MS = 22
        MS_20 = 23
        MT = 24
        MUN = 25
        MW = 26
        MWB = 27
        MWC = 28
        MWP = 29
        MWR = 30
        MWW = 31
        NO = 32
        UK = 33
        UNKNOWN = 34

        __labels__ = {
            TWO: _('2'),
            FOUR: _('4'),
            FA: _('fa'),
            H: _('H'),
            LG: _('lg'),
            M: _('m'),
            MA: _('ma'),
            mb: ('mb'),
            MBLG: _('MbLg'),
            MB_LG: _('Mb_lg'),
            MC: _('mc'),
            MD: ('md'),
            MDL: _('mdl'),
            ME: _('Me'),
            MFA: _('mfa'),
            MH: _('mh'),
            MI: _('Mi'),
            MINT: _('mint'),
            ML: _('ml'),
            MLG: _('mlg'),
            MLR: _('mlr'),
            MLV: _('mlv'),
            MS: _('Ms'),
            MS_20: _('ms_20'),
            MT: _('Mt'),
            MUN: _('mun'),
            MW: _('mw'),
            MWB: _('mwb'),
            MWC: _('mwc'),
            MWP: _('mwp'),
            MWR: _('mwr'),
            MWW: _('mwm'),
            NO: _('no'),
            UK: _('uk'),
            UNKNOWN: _('Unknown')

        }

    event_title = models.CharField(max_length=255, verbose_name=_('event title'))
    event_place = models.CharField(max_length=255, verbose_name=_('event place'))
    event_date = models.DateTimeField(
        verbose_name=_('event date'),
        null=True, blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        null=True, blank=True
    )
    latitude = models.FloatField(verbose_name=_('latitude'))
    longitude = models.FloatField(verbose_name=_('longitude'))
    depth = models.FloatField(verbose_name=_('depth'))
    magnitude = models.FloatField(verbose_name=_('magnitude'))
    magnitude_type = enum.EnumField(MagnitudeType)

    def __str__(self):
        return f'{self.event_title} - {self.magnitude}'
