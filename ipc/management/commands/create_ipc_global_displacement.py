from django.core.management.base import BaseCommand
from django.db import models

from ipc.models import (
    IpcMonthly,
    GlobalDisplacement,
    Country
)


class Command(BaseCommand):
    help = 'Create global displacement from ipc for food_insecurity'

    def handle(self, *args, **options):
        queryset = IpcMonthly.objects.all()
        if queryset.filter(phase_population__isnull=False, is_projected=True).distinct().exists():
            queryset = queryset.values('country', 'analysis_date').annotate(
                total_displacement=models.Sum('phase_population')
            ).values(
                'total_displacement',
                'country_id',
                'hazard_type',
                'analysis_date',
                'year',
                'month'
            )
            for d in queryset:
                data = {
                    'country': Country.objects.get(id=d['country_id']),
                    'total_displacement': d['total_displacement'],
                    'hazard_type': d['hazard_type'],
                    'year': d['year'],
                    'month': d['month']
                }
                if not GlobalDisplacement.objects.filter(country=data['country'], year=data['year'], month=data['month']).exists():
                    GlobalDisplacement.objects.create(**data)
