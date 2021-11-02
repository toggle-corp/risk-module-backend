import pandas as pd

from django.core.management.base import BaseCommand
from django.db import models
from django.utils import timezone

from ipc.models import Ipc, GlobalDisplacement, Country


class Command(BaseCommand):
    help = 'Create global displacement from ipc for food_insecurity'

    def handle(self, *args, **options):
        queryset = Ipc.objects.filter(is_projected=True).values('country', 'analysis_date', 'title').annotate(
            total_displacement=models.Sum('phase_population')
        ).values(
            'total_displacement',
            'country_id',
            'hazard_type',
            'analysis_period_start_date',
            'analysis_period_end_date'
        )
        for d in queryset:
            date_range = pd.date_range(d['analysis_period_start_date'], d['analysis_period_end_date'], freq='MS')
            for range in date_range:
                year = int(range.strftime('%Y'))
                month = int(range.strftime('%m'))
                data = {
                    'country': Country.objects.get(id=d['country_id']),
                    'total_displacement': d['total_displacement'],
                    'hazard_type': d['hazard_type'],
                    'year': year,
                    'month': month
                }
                GlobalDisplacement.objects.create(**data)
