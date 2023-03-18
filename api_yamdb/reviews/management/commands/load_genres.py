from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Genre


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Genre.objects.exists():
            print('Все данные в таблицу Genre уже загружены')
            return

        for row in DictReader(open('static/data/genre.csv')):
            genre = Genre(id=row['id'],
                          name=row['name'],
                          slug=row['slug'],
                          )
            genre.save()

        print('Данные в таблицу Genre успешно загружены')
