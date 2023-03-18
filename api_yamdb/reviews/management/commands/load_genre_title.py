from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import GenreTitle


class Command(BaseCommand):
    def handle(self, *args, **options):
        if GenreTitle.objects.exists():
            print('Все данные в таблицу GenreTitle уже загружены')
            return

        for row in DictReader(open('static/data/genre_title.csv')):
            genre_title = GenreTitle(id=row['id'],
                                     genre_id=row['genre_id'],
                                     title_id=row['title_id'],
                                     )
            genre_title.save()

        print('Данные в таблицу GenreTitle успешно загружены')
