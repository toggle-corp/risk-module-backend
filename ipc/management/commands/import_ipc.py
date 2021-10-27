import datetime
import logging
import requests

from django.core.management.base import BaseCommand

from ipc.models import Ipc, Country
from oddrin.models import Oddrin


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import Ipc Data'

    def parse_date(self, date):
        if date:
            return datetime.datetime.strptime(date, '%b %Y').strftime('%Y-%m-01')

    def parse_analysis_date(self, date):
        return datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8])).strftime('%Y-%m-%d')

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

                    data = {
                        'title': data['title'],
                        'country': country,
                        'analysis_date': self.parse_analysis_date(data['fanalysis_date']),
                        'phase_population': data['p3_plus_population'],
                        'census_population': data['census_population'],
                        'current_from_date': self.parse_date(data['current_from_date']),
                        'current_to_date': self.parse_date(data['current_thru_date']),
                        'projected_from_date': self.parse_date(data['projected_from_date']),
                        'projected_to_date': self.parse_date(data['projected_thru_date']),
                        'hazard_type': Oddrin.HazardType.FOOD_INSECURITY
                    }
                    Ipc.objects.create(**data)
