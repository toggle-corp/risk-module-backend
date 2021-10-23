import datetime
import logging
import requests

from django.core.management.base import BaseCommand

from ipc.models import Ipc

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import Ipc Data'

    def parse_date(self, date):
        if date:
            return datetime.datetime.strptime(date, '%b %Y').strftime('%Y-%m-01')

    def handle(self, *args, **options):
        for i in range(1, 9):
            ipc_url = f"http://mapipcissprd.us-east-1.elasticbeanstalk.com/api/public/population-tracking-tool/data/2017,2021/?page={i}&limit=20&condition=A"
            response = requests.get(ipc_url)
            if response.status_code != 200:
                error_log = f'Error querying ipc data at {ipc_url}'
                logger.error(error_log)
                logger.error(response.content)
            ipc_data = response.json()
            for data in ipc_data:
                data = {
                    'title': data['title'],
                    'country_code': data['code'],
                    'country': data['country'],
                    'analysis_date': self.parse_date(data['analysis_date']),
                    'phase_popultion': data['p3_plus_population'],
                    'census_population': data['census_population'],
                    'current_from_date': self.parse_date(data['current_from_date']),
                    'current_to_date': self.parse_date(data['current_thru_date']),
                    'projected_from_date': self.parse_date(data['projected_from_date']),
                    'projected_to_date': self.parse_date(data['projected_thru_date']),
                }
                Ipc.objects.get_or_create(**data)