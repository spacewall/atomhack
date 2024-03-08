import csv

import names

from django.core.management.base import BaseCommand
from mars_client.models import Report


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('reports.csv', 'r') as file:
            reports = list(csv.DictReader(file, delimiter=';'))

            for report in reports:
                Report(**report).save()
