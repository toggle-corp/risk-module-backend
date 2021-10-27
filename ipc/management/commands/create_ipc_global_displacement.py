from dateutil.relativedelta import relativedelta
import pandas as pd

from django.core.management.base import BaseCommand
from django.db import models
from django.utils import timezone

from ipc.models import Ipc, GlobalDisplacement, Country


class Command(BaseCommand):
    help = 'Create global displcement from ipc for food_insecurity'

    def handle(self, *args, **options):
        three_months_prior = timezone.now() + relativedelta(months=-3)
        queryset = Ipc.objects.exclude(analysis_date__lte=three_months_prior)
        data = queryset.values('country', 'analysis_date', 'title').annotate(
            total_displacement=models.Sum('phase_population')
        ).values(
            'total_displacement',
            'country_id',
            'hazard_type',
            'current_from_date',
            'current_to_date'
        )
        for d in data:
            date_range = pd.date_range(d['current_from_date'], d['current_to_date'], freq='MS')
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
