import requests
import datetime
import logging

from django.core.management.base import BaseCommand

from earthquake.models import Earthquake


class Command(BaseCommand):
    help = 'Import Earthquake geo-locations from external api'

    def parse_timestamp(self, timestamp):
        # NOTE: all timestamp are in millisecond and with timezone `utc`
        format = "%Y-%m-%dT%H:%M:%S%z"
        return datetime.datetime.utcfromtimestamp(timestamp/1000).strftime(format)

    def handle(self, *args, **options):
        logging.info('Starting data import')
        # NOTE: This is for the local test purpose only
        url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02'
        response = requests.get(url)
        if response.status_code != 200:
            error_log = f'Error querying earthquake data at {url}'
            logging.error(error_log)
            logging.error(response.content)
        earthquake_data = response.json()
        for earthquake in earthquake_data['features']:
            data = {
                'id': earthquake['id'],
                'event_title': earthquake['properties']['title'],
                'event_place': earthquake['properties']['place'],
                'event_date': self.parse_timestamp(earthquake['properties']['time']),
                'updated_at': self.parse_timestamp(earthquake['properties']['updated']),
                'latitude': earthquake['geometry']['coordinates'][1],
                'longitude': earthquake['geometry']['coordinates'][0],
                'depth': earthquake['geometry']['coordinates'][2],
                'magnitude': earthquake['properties']['mag'],
                'magnitude_type': earthquake['properties']['magType']
            }
            Earthquake.objects.create(**data)
        added = Earthquake.objects.count()
        logging.info(f'Added Earthquake data count {added}')
