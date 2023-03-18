from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import Review


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Review.objects.exists():
            print('Все данные в таблицу Review уже загружены')
            return

        for row in DictReader(open('static/data/review.csv')):
            review = Review(id=row['id'],
                            title_id=row['title_id'],
                            text=row['text'],
                            author_id=row['author'],
                            score=row['score'],
                            pub_date=row['pub_date'],
                            )
            review.save()

        print('Данные в таблицу Review успешно загружены')
