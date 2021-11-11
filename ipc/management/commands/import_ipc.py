import datetime
import logging
import requests

from django.core.management.base import BaseCommand

from ipc.models import Ipc, Country
from oddrin.models import HazardType


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import Ipc Data'

    def parse_date(self, date):
        if date:
            return datetime.datetime.strptime(date, '%b %Y').strftime('%Y-%m-01')

    def get_month(self, analysis_period_start_date, analysis_date):
        analysis_period_start_date = datetime.datetime.strptime(analysis_period_start_date, '%Y-%m-%d')
        analysis_date = datetime.datetime.strptime(analysis_date, '%Y-%m-%d')
        return abs(analysis_period_start_date.month - analysis_date.month)

    def handle(self, *args, **options):
        for i in range(1, 9):
            ipc_url = f"http://mapipcissprd.us-east-1.elasticbeanstalk.com/api/public/population-tracking-tool/data/2017,2021/?page={i}&limit=200000&condition=A"
            response = requests.get(ipc_url)
            if response.status_code != 200:
                error_log = f'Error querying ipc data at {ipc_url}'
                logger.error(error_log)
                logger.error(response.content)
            ipc_data = response.json()
            for data in ipc_data:
                # Check whether is the country is present in local country
                if Country.objects.filter(name=data['country']).exists():
                    country = Country.objects.get(name=data['country'])
                    analysis_period = data['analysis_period'].split('-')
                    analysis_period_start_date = analysis_period[0].strip()
                    analysis_period_end_date = analysis_period[1].strip()
                    data = {
                        'title': data['title'],
                        'country': country,
                        'analysis_date': self.parse_date(data['analysis_date']),
                        'phase_population': data['p3_plus_population'],
                        'census_population': data['census_population'],
                        'analysis_period_start_date': self.parse_date(analysis_period_start_date),
                        'analysis_period_end_date': self.parse_date(analysis_period_end_date),
                        'hazard_type': HazardType.FOOD_INSECURITY
                    }
                    month = self.get_month(data['analysis_period_start_date'], data['analysis_date'])
                    if data['analysis_period_end_date'] and data['analysis_date'] > data['analysis_period_end_date']:
                        data['is_projected'] = False
                        Ipc.objects.create(**data)
                    elif data['analysis_period_start_date'] and data['analysis_date'] < data['analysis_period_start_date'] and month < 3:
                        data['is_projected'] = True
                        Ipc.objects.create(**data)
