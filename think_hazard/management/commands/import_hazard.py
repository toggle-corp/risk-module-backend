import logging
import csv
import os
import requests

from django.core.management.base import BaseCommand, CommandError

from think_hazard.models import (
    ThinkHazardCountry,
    Hazard
)

logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Import think_hazard data'

    def handle(self, *args, **options):
        # lets list all the countries availabel
        country_list = ThinkHazardCountry.objects.first()
        logger.info('Starting data import')
        url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={seven_days_before}&endtime={today}'
        response = requests.get(url)
        if response.status_code != 200:
            error_log = f'Error querying earthquake data at {url}'
            logger.error(error_log)
            logger.error(response.content)