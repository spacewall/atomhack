import csv, random, string

import names

from django.core.management.base import BaseCommand
from mars_client.models import Report


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        def randomword(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))
        
        for _ in range(10):
            Report(name_and_surname=names.get_full_name(gender='man'), context=randomword(10)).save()
