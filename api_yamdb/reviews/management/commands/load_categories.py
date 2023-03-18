from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Category.objects.exists():
            print('Все данные в таблицу Category уже загружены')
            return

        for row in DictReader(open('static/data/category.csv')):
            category = Category(id=row['id'],
                                name=row['name'],
                                slug=row['slug'],
                                )
            category.save()

        print('Данные в таблицу Category успешно загружены')
