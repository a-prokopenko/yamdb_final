from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Title


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Title.objects.exists():
            print('Все данные в таблицу Title уже загружены')
            return

        for row in DictReader(open('static/data/titles.csv')):
            title = Title(id=row['id'],
                          name=row['name'],
                          year=row['year'],
                          category_id=row['category'],
                          )
            title.save()

        print('Данные в таблицу Title успешно загружены')
