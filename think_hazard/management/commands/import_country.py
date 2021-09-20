import logging
import csv
import os

from django.core.management.base import BaseCommand, CommandError

from think_hazard.models import ThinkHazardCountry

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import Country with iso code from ThinkHazard'
    missing_args_message = "Filename is missing. A valid CSV file is required."

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        pre = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(pre, options['filename'][0])
        if not os.path.exists(filename):
            raise CommandError("%s doesnt exist." % filename)
        with open(filename, 'r') as csvfile:
            csv_file = csv.reader(csvfile, delimiter=';')
            next(csv_file)
            logger.info('Starting country import')
            count = 0
            for row in csv_file:
                ThinkHazardCountry.objects.get_or_create(
                    country_code=row[0],
                    country=row[1],
                    iso3=row[3]
                )
                count += count
        logger.info(f'Imported {count} countries')
