import logging
import requests

from django.core.management.base import BaseCommand

from think_hazard.models import (
    ThinkHazardCountry,
    Hazard,
    HazardInformation
)

logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Import think_hazard data'

    def handle(self, *args, **options):
        # lets list all the countries available
        country_list = ThinkHazardCountry.objects.values_list('country_code', 'id')
        for country_code, country_id in country_list:
            logger.info('Starting data import')
            count = 0
            url = f'http://thinkhazard.org/en/report/{country_code}.json'
            response = requests.get(url)
            if response.status_code != 200:
                error_log = f'Error querying earthquake data at {url}'
                logger.error(error_log)
                logger.error(response.content)

            list_of_dicts = []
            hazard = Hazard.objects.create(country_id=country_id)
            data = response.json()
            for x in range(len(data)):
                hazard_type = data[x]['hazardtype']['mnemonic']
                hazard_level = data[x]['hazardlevel']['mnemonic']
                list_of_dicts.append({'hazard_type': hazard_type, 'hazard_level': hazard_level})
            for data in list_of_dicts:
                obj, created= HazardInformation.objects.get_or_create(
                    hazard_type=data['hazard_type'],
                    hazard_level=data['hazard_level']
                )
                hazard.hazard_informations.add(obj)
                hazard.save()
                count += count
        logger.info(f'Imported {count} number of countries hazard')
