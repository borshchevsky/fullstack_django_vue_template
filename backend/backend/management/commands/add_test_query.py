# adding a test query to work with a frontend
# this file should be removed

from django.core.management.base import BaseCommand, CommandError
from backend.models import TestModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_query = TestModel(name='testname')
        test_query.save()

        self.stdout.write(
            self.style.SUCCESS(f'Test query created {test_query.id}')
        )