import requests
import logging
import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from oddrin.models import HazardType, Pdc


logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Import Active Hazards'

    def parse_timestamp(self, timestamp):
        # NOTE: all timestamp are in millisecond and with timezone `utc`
        return timezone.make_aware(datetime.datetime.utcfromtimestamp(int(timestamp)/1000))

    def handle(self, *args, **options):
        access_token = 'eyJraWQiOiIyMDE4LTA0LTA1fHRlc3RhcHBzLnBkYy5vcmciLCJhbGciOiJSUzUxMiJ9.eyJqdGkiOiJkNzM1MDk4NS1mMDZiLTQyZGUtYjhhYi1mMDg5ZGU3YmNhY2MiLCJpc3MiOiJodHRwczovL3Rlc3RhcHBzLnBkYy5vcmcvand0L2p3a3MuanNvbiIsImlhdCI6MTYzOTA5OTI3NywibmJmIjoxNjM5MDk5Mjc3LCJzdWIiOiJ0ZXN0YXBwcy5wZGMub3JnIiwiZXhwIjo0MTAyNDQ0ODAwLCJ1c2VyUm9sZXMiOlsiTE9HSU4iXSwidXNlckdyb3VwSWQiOiIyIiwidG9rZW5UeXBlIjoibG9uZyJ9.U4PEr83nLptbQ0OIKWhGGuokYN9FkfMociiBrYCe4v8j7yvG-1RzM-ETCqi8t7U-TTiIk9AA4bKAl72Tf30mtNC42etpga7wStOUpzHnmJ32WkYw9xocMQhJIuORz4aVDNjlyhsO2nyTGOpZWy4EFQVhUkw3Zx0Ka8K0HZ0JTN1kaQuAMg2JciL8Y1mKNKE9f0rWIg0UM80FF1Rt_R1x9HtioXzA3pVRZTOcgN5Fydv6NEaR8NonTaXigt1p_1NFuw3RuAJffqfgvgKnyi8aEUYo_Ec6J_i3vSmJrcX2_kV0H7L-vzJK1mHl-lZNG0ytJw3GZQiCIsI4kzGJcr4NiA'
        url = 'https://testsentry.pdc.org/hp_srv/services/hazards/t/json/get_active_hazards'
        headers = {'Authorization': "Bearer {}".format(access_token)}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            error_log = f'Error querying PDC data at {url}'
            logger.error(error_log)
            logger.error(response.content)
        response_data = response.json()
        for data in response_data:
            hazard_type = data['type_ID']
            if hazard_type == 'FLOOD':
                hazard_type = HazardType.FLOOD
                data = {
                    'hazard_id': data['hazard_ID'],
                    'hazard_name': data['hazard_Name'],
                    'latitude': data['latitude'],
                    'longitude': data['longitude'],
                    'description': data['description'],
                    'hazard_type': hazard_type,
                    'uuid': data['uuid'],
                    'start_date': self.parse_timestamp(data['start_Date']),
                    'end_date': self.parse_timestamp(data['end_Date'])
                }
                Pdc.objects.create(**data)
            elif hazard_type == 'CYCLONE':
                hazard_type = HazardType.CYCLONE
                data = {
                    'hazard_id': data['hazard_ID'],
                    'hazard_name': data['hazard_Name'],
                    'latitude': data['latitude'],
                    'longitude': data['longitude'],
                    'description': data['description'],
                    'hazard_type': hazard_type,
                    'uuid': data['uuid'],
                    'start_date': self.parse_timestamp(data['start_Date']),
                    'end_date': self.parse_timestamp(data['end_Date'])
                }
                Pdc.objects.create(**data)
            elif hazard_type == 'STORM':
                hazard_type = HazardType.STORM
                data = {
                    'hazard_id': data['hazard_ID'],
                    'hazard_name': data['hazard_Name'],
                    'latitude': data['latitude'],
                    'longitude': data['longitude'],
                    'description': data['description'],
                    'hazard_type': hazard_type,
                    'uuid': data['uuid'],
                    'start_date': self.parse_timestamp(data['start_Date']),
                    'end_date': self.parse_timestamp(data['end_Date'])
                }
                Pdc.objects.create(**data)
            elif hazard_type == 'DROUGHT':
                hazard_type = HazardType.DROUGHT
                data = {
                    'hazard_id': data['hazard_ID'],
                    'hazard_name': data['hazard_Name'],
                    'latitude': data['latitude'],
                    'longitude': data['longitude'],
                    'description': data['description'],
                    'hazard_type': hazard_type,
                    'uuid': data['uuid'],
                    'start_date': self.parse_timestamp(data['start_Date']),
                    'end_date': self.parse_timestamp(data['end_Date'])
                }
                Pdc.objects.create(**data)
            elif hazard_type == 'WIND':
                hazard_type = HazardType.WIND
                data = {
                    'hazard_id': data['hazard_ID'],
                    'hazard_name': data['hazard_Name'],
                    'latitude': data['latitude'],
                    'longitude': data['longitude'],
                    'description': data['description'],
                    'hazard_type': hazard_type,
                    'uuid': data['uuid'],
                    'start_date': self.parse_timestamp(data['start_Date']),
                    'end_date': self.parse_timestamp(data['end_Date'])
                }
                Pdc.objects.create(**data)
            elif hazard_type == 'TSUNAMI':
                hazard_type = HazardType.TSUNAMI
                data = {
                    'hazard_id': data['hazard_ID'],
                    'hazard_name': data['hazard_Name'],
                    'latitude': data['latitude'],
                    'longitude': data['longitude'],
                    'description': data['description'],
                    'hazard_type': hazard_type,
                    'uuid': data['uuid'],
                    'start_date': self.parse_timestamp(data['start_Date']),
                    'end_date': self.parse_timestamp(data['end_Date'])
                }
                Pdc.objects.create(**data)
            elif hazard_type == 'EARTHQUAKE':
                hazard_type = HazardType.EARTHQUAKE
                data = {
                    'hazard_id': data['hazard_ID'],
                    'hazard_name': data['hazard_Name'],
                    'latitude': data['latitude'],
                    'longitude': data['longitude'],
                    'description': data['description'],
                    'hazard_type': hazard_type,
                    'uuid': data['uuid'],
                    'start_date': self.parse_timestamp(data['start_Date']),
                    'end_date': self.parse_timestamp(data['end_Date'])
                }
                Pdc.objects.create(**data)
